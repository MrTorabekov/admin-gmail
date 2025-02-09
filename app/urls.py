from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.urls import path
from app.views import (
    DoctorAPIView,
    NewsAPIView,
    RegisterAPIView,
    LoginApiView,
    UserUpdateAPIView,
    DoctorFilterView,
    DoctorUpdateAPIView,
    BookingAPIView,
    DoctorDateAPIView
)

urlpatterns = [
    path('doctor/', DoctorAPIView.as_view(), name='doctors-list'),
    path('doctor/<int:pk>', DoctorAPIView.as_view(), name='doctors-detail'),
    path('doctor/update/<int:pk>', DoctorUpdateAPIView.as_view(), name='doctor-update'),
    path('news/<int:pk>', NewsAPIView.as_view(), name='news-detail'),
    path('news/', NewsAPIView.as_view(), name='news-detail'),
    path("search/", DoctorFilterView.as_view(), name='search'),
    path('date', DoctorDateAPIView.as_view(), name='doctor-date'),
    path('booking/<int:pk>', BookingAPIView.as_view(), name='booking-list'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path("users/update/<int:pk>/", UserUpdateAPIView.as_view(), name="users"),
    path('login/', LoginApiView.as_view(), name="login"),
    path('register', RegisterAPIView.as_view(), name='doctors-register'),

]