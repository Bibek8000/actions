from django.urls import path
from rest_framework_simplejwt.views import(TokenObtainPairView, TokenRefreshView)
from .views import DashboardAPIView
urlpatterns = [
    path('api/token/',TokenObtainPairView.as_view()),
    path('api/refresh/',TokenRefreshView.as_view()),
    path('api/dashboard/',DashboardAPIView.as_view()),

    
]

