from django.urls import path
from .import api_views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)

urlpatterns = [
    path('jobAPI/',api_views.JobAPI.as_view()),
    path('jobdetailAPI/<int:pk>/',api_views.JobDetailAPI.as_view()),
    path("register/",api_views.Register.as_view(), name="register"),
    path("apply/<int:pk>/",api_views.ApplyAPI.as_view(), name="apply"),
    path("myapplication/",api_views.MyApplicationAPI.as_view(), name="myapplications"),
    path("applicantsapi/<int:pk>/",api_views.ApplicantsAPI.as_view()),



    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),

    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),  
]