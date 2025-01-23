from rest_framework import serializers
from app.models import Doctor,User,News

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','avatar']


class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Doctor
        fields = ['user','specialization','experience','location','clinic_name','consultation_fee','is_consultation_fee','available_today','rating_percentage','patient_stories']



class NewsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:

        model = News
        fields = ['user','title','img','created_at']

