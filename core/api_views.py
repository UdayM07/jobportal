from django.shortcuts import get_object_or_404

from rest_framework import filters, generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import Job, Application
from .serializers import (
    JobSerializer,
    RegisterSerializer,
    ApplicationSerializer,
)
from .permissions import IsRecruiter


# ---------------- Job API ----------------

class JobAPI(generics.ListCreateAPIView):

    queryset = Job.objects.all().order_by("-created_at")

    serializer_class = JobSerializer

    permission_classes = [IsRecruiter]

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]

    ordering_fields = [
        "salary",
        "created_at",
        "title",
    ]

    search_fields = [
        "title",
        "company",
    ]

    filterset_fields = [
        "location",
        "job_type",
        "experience",
        "company",
    ]

    def perform_create(self, serializer):

        serializer.save(
            created_by=self.request.user,
            company=self.request.user.company
        )


# ---------------- Job Detail API ----------------

class JobDetailAPI(generics.RetrieveUpdateDestroyAPIView):

    queryset = Job.objects.all()

    serializer_class = JobSerializer

    permission_classes = [IsRecruiter]


# ---------------- Register API ----------------

class api_Register(generics.CreateAPIView):

    serializer_class = RegisterSerializer


# ---------------- Apply Job API ----------------

class ApplyAPI(generics.CreateAPIView):

    queryset = Application.objects.all()

    serializer_class = ApplicationSerializer

    def perform_create(self, serializer):

        job = get_object_or_404(
            Job,
            pk=self.kwargs["pk"],
        )

        serializer.save(
            job=job,
            candidate=self.request.user,
        )


# ---------------- My Applications API ----------------

class MyApplicationAPI(generics.ListAPIView):

    serializer_class = ApplicationSerializer

    def get_queryset(self):

        return (
            Application.objects
            .filter(candidate=self.request.user)
            
            .order_by("-applied_at")
        )


# ---------------- Applicants API ----------------

class ApplicantsAPI(generics.ListAPIView):

    serializer_class = ApplicationSerializer

    def get_queryset(self):

        job = get_object_or_404(
            Job,
            pk=self.kwargs["pk"],
            created_by=self.request.user,
        )

        return (
            Application.objects
            .filter(job=job)
            
            .order_by("-applied_at")
        )