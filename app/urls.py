from django.urls import path
from app.views import DoctorAPIView,NewsAPIView,DoctorFilterView,RegisterAPIView,LoginApiView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('doctor/', DoctorAPIView.as_view(), name='doctors-list'),
    path('doctor/<int:pk>', DoctorAPIView.as_view(), name='doctors-detail'),
    path('news/<int:pk>', NewsAPIView.as_view(), name='news-detail'),
    path('register', RegisterAPIView.as_view(), name='doctors-register'),
    path('news/', NewsAPIView.as_view(), name='news-detail'),
    path("search", DoctorFilterView.as_view(), name='search'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('login/', LoginApiView.as_view(), name="login"),

]
