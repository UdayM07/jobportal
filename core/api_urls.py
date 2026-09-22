from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import api_views


urlpatterns = [
    path(
        "jobAPI/",
        api_views.JobAPI.as_view(),
        name="job_api",
    ),

    path(
        "jobdetailAPI/<int:pk>/",
        api_views.JobDetailAPI.as_view(),
        name="job_detail_api",
    ),

    path(
        "api_register/",
        api_views.api_Register.as_view(),
        name="api_register",
    ),

    path(
        "apply/<int:pk>/",
        api_views.ApplyAPI.as_view(),
        name="apply_api",
    ),

    path(
        "myapplication/",
        api_views.MyApplicationAPI.as_view(),
        name="my_application_api",
    ),

    path(
        "applicantsapi/<int:pk>/",
        api_views.ApplicantsAPI.as_view(),
        name="applicants_api",
    ),

    path(
        "token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),

    path(
        "token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
]