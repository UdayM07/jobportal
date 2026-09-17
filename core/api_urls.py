from django.urls import path
from .import api_views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)

urlpatterns = [
    path('jobAPI/',api_views.JobAPI.as_view()),
    path('jobdetailAPI/<int:pk>/',api_views.JobDetailAPI.as_view()),
    path("api_register/",api_views.api_Register.as_view()),
    path("apply/<int:pk>/",api_views.ApplyAPI.as_view()),
    path("myapplication/",api_views.MyApplicationAPI.as_view()),
    path("applicantsapi/<int:pk>/",api_views.ApplicantsAPI.as_view()),



    path("token/", TokenObtainPairView.as_view()),

    path("token/refresh/", TokenRefreshView.as_view()),  
]