from drf_spectacular.utils import extend_schema,OpenApiParameter
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.throttling import UserRateThrottle
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from app.models import Doctor,News,User,Booking
from django_filters.rest_framework import DjangoFilterBackend
from app.serializers import (
    DoctorSerializer,
    NewsSerializer,
    RegisterSerializer,
    LoginSerializer,
    UserUpdateSerializer,
    DoctorUpdateSerializer,
    BookingSerializer
)


class DoctorAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    throttle_classes = [UserRateThrottle]
    def get(self, request, pk=None):
        if pk:
            try:
                doctor = Doctor.objects.get(pk=pk)
                serializer = DoctorSerializer(doctor)
                return Response(serializer.data)
            except Doctor.DoesNotExist:
                return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            doctor = Doctor.objects.all()
            serializer = DoctorSerializer(doctor, many=True)
            return Response(serializer.data)

class NewsAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                news = News.objects.get(pk=pk)
                serializer = NewsSerializer(news)
                return Response(serializer.data)
            except Doctor.DoesNotExist:
                return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            news = News.objects.all()
            serializer = NewsSerializer(news, many=True)
            return Response(serializer.data)

class DoctorFilterView(ListAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields = ['location', 'clinic_name']
    filterset_fields = ['experience', 'rating_percentage', 'consultation_fee', 'location']

class DoctorListApiView(APIView):

    def get(self,request):
        doctors = Doctor.object.all()
        serializer = DoctorSerializer(doctors,many=True)
        return Response(serializer.data)

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(password=make_password(serializer.validated_data['password']))
            # Generate jwt

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({
                    'refresh': str(refresh),
                    'access': access_token,
                    'username': serializer.data
                }, status=status.HTTP_201_CREATED
            )

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginApiView(APIView):
    @extend_schema(
        summary="User Login",
        description="Login using email and password to obtain JWT tokens.",
        request=LoginSerializer,
        responses={
        200: OpenApiParameter(name="Tokens",description="JWT access and refresh tokens"),
        400: OpenApiParameter(name="Error",description="Invalid credentials or validation errors"),
        },
        tags=["User Authentication"]

    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get("email")
            password = serializer.validated_data.get("password")

            user = User.objects.get(email=email)
            if user.check_password(password):
                if not user.is_active:
                    return Response({"detail": "User accaunt is inactive."}, status=status.HTTP_400_BAD_REQUEST)
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)

                return Response({
                    "refresh": str(refresh),
                    "access": access_token,
                }, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserUpdateAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    @extend_schema(
        summary="User Registration",
        description="Register user",
        request=UserUpdateSerializer,
        responses={
            200: OpenApiParameter(name="User Updated", description="User data updated"),
            400: OpenApiParameter(name="Errors", description="Invalid credentials")
        },
        tags=["User Update"]
    )
    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserUpdateSerializer(instance=user, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoctorUpdateAPIView(APIView):
    @extend_schema(
        summary="Doctor Update API View",
        description="Doctor Update Data",
        request=DoctorUpdateSerializer,
        responses={
            200: OpenApiParameter(name="Doctor Update", description="Doctor Update APi View data"),
            400: OpenApiParameter(name="Errors", description="Invalid credentials")
        },
        tags=["Doctor"]
    )
    def put(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        serializer = DoctorUpdateSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoctorDeleteAPIView(APIView):
    def delete(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        doctor.delete()
        return Response({'message': 'Doctor has been deleted successfully'}, status=status.HTTP_200_OK)

class BookingAPIView(APIView):
    def get(self, request):
        booking = Booking.objects.all()
        serializer = BookingSerializer(booking, many=True)
        return Response(serializer.data)