from django.urls import path
from app.views import DoctorAPIView,NewsAPIView
urlpatterns = [
    path('doctor/', DoctorAPIView.as_view(), name='doctors-list'),
    path('doctor/<int:pk>', DoctorAPIView.as_view(), name='doctors-detail'),
    path('news/<int:pk>', NewsAPIView.as_view(), name='news-detail'),
    path('news/', NewsAPIView.as_view(), name='news-detail'),
]
