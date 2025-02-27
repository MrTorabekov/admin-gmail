from datetime import timedelta

from django.utils.timezone import now
from rest_framework import serializers

from app.models import Doctor, User, News,Date
from roots import settings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','avatar']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.avatar:
            representation['avatar'] = settings.BASE_URL + instance.avatar.url
        else:
            representation['avatar'] = None
        return representation

class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Doctor
        fields = ['user','specialization','experience','location','clinic_name','consultation_fee','is_consultation_fee','availability_today','rating_percentage','patient_stories']

class NewsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    img = serializers.SerializerMethodField()
    class Meta:

        model = News
        fields = ['user','title','img','created_at']

    def get_img(self,obj):
        if obj.img:
            return settings.BASE_URL + obj.img.url
        return None

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','password','role')

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class UserUpdateSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "avatar"]

class DoctorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['specialization', 'experience', 'location', 'clinic_name', 'consultation_fee',
                  'is_consultation_fee', 'availability_today']

class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Date
        fields = ['id','user', 'doctor', 'date','time', 'status']


class DateSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Date
        fields = ['id','user', 'doctor', 'date','time', 'status','created_at']


