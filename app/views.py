from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import Doctor,News
from django_filters.rest_framework import DjangoFilterBackend
from app.serializers import DoctorSerializer,NewsSerializer

class DoctorAPIView(APIView):
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
