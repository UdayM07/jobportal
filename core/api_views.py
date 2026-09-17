from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404



from .models import Job,Application
from .serializers import JobSerializer,RegisterSerializer,ApplicationSerializer
from .permissions import IsRecruiter


class JobAPI(generics.ListCreateAPIView):

    # -------------------------------
    # queryset
    # -------------------------------
    # Fixed DRF attribute.
    #
    # Responsibility:
    # Tells DRF which objects should be used.
    #
    # Internally:
    # GET  -> queryset -> serializer -> response
    # POST -> not used for creating directly, but DRF still knows
    #         which model this view belongs to.
    #
    queryset = Job.objects.all()


    # -------------------------------
    # serializer_class
    # -------------------------------
    # Fixed DRF attribute.
    #
    # Responsibility:
    # Which serializer should DRF use?
    #
    # Internally:
    #
    # GET
    # queryset
    #      ↓
    # JobSerializer(instance=queryset)
    #      ↓
    # JSON Response
    #
    # POST
    # Incoming JSON
    #      ↓
    # JobSerializer(data=request.data)
    #      ↓
    # Validation
    #      ↓
    # Save()
    #
    serializer_class = JobSerializer


    # -------------------------------
    # permission_classes
    # -------------------------------
    # Fixed DRF attribute.
    #
    # Responsibility:
    # Before executing the view,
    # DRF checks these permission classes.
    #
    # Internally:
    #
    # Request
    #     ↓
    # Authentication (JWT)
    #     ↓
    # request.user
    #     ↓
    # IsRecruiter.has_permission()
    #     ↓
    # Allowed / Denied
    #
    permission_classes = [IsRecruiter]


    # -------------------------------
    # filter_backends
    # -------------------------------
    # Fixed DRF attribute.
    #
    # Responsibility:
    # Which filtering system should DRF run?
    #
    # DRF executes these backends one by one.
    #
    # SearchFilter
    #     -> handles ?search=
    #
    # DjangoFilterBackend
    #     -> handles ?location=
    #     -> handles ?job_type=
    #     -> handles ?experience=
    #
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


    # -------------------------------
    # search_fields
    # -------------------------------
    # Fixed DRF attribute.
    #
    # Responsibility:
    # Which model fields are searchable?
    #
    # Example:
    #
    # /api/jobAPI/?search=python
    #
    # DRF searches:
    #
    # title
    # company.name
    #
    search_fields = [
        "title",
        "company__name",
    ]


    # -------------------------------
    # filterset_fields
    # -------------------------------
    # Fixed DRF attribute.
    #
    # Responsibility:
    # Which fields allow exact filtering?
    #
    # Example:
    #
    # ?location=Bangalore
    #
    # ?job_type=Full Time
    #
    # ?experience=Fresher
    #
    # ?company=1
    #
    filterset_fields = [
        "location",
        "job_type",
        "experience",
        "company",
    ]

    # pagination_class=JobPagination


    # -------------------------------
    # perform_create()
    # -------------------------------
    # Fixed GenericAPIView method.
    #
    # Called automatically ONLY during POST.
    #
    # Why?
    #
    # Because serializer.save()
    # normally only saves request.data.
    #
    # But created_by is NOT coming from user input.
    #
    # We want:
    #
    # created_by=request.user
    #
    # automatically.
    #
    def perform_create(self, serializer):

        serializer.save(
            created_by=self.request.user
        )


class JobDetailAPI(generics.RetrieveUpdateDestroyAPIView):

    # Used by GET(id), PUT, PATCH and DELETE.
    queryset = Job.objects.all()

    # Converts Model ↔ JSON.
    serializer_class = JobSerializer

    # Runs has_permission() first.
    # Then has_object_permission().
    permission_classes = [IsRecruiter]



class api_Register(generics.CreateAPIView):
    serializer_class=RegisterSerializer

class ApplyAPI(generics.CreateAPIView):
    queryset=Application.objects.all()
    serializer_class=ApplicationSerializer

    def perform_create(self, serializer):
        job=get_object_or_404(Job,pk=self.kwargs['pk'])
        serializer.save(
            job=job,
            candidate=self.request.user
        )

class MyApplicationAPI(generics.ListAPIView):
    serializer_class = ApplicationSerializer

    def get_queryset(self):


        return Application.objects.filter(
            candidate=self.request.user
        )


class ApplicantsAPI(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    
    def get_queryset(self):
        job=get_object_or_404(Job,
                              pk=self.kwargs['pk'],
                              created_by=self.request.user
                            )

        return Application.objects.filter(
            job=job,
            
        )


    




