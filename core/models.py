from django.db import models
from django.contrib.auth.models import AbstractUser


class Company(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="company_logos/", blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    location = models.CharField(max_length=150)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class User(AbstractUser):

    ROLE_CHOICES = (
        ("Candidate", "Candidate"),
        ("Recruiter", "Recruiter"),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="Candidate",
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="recruiters",
    )

    def __str__(self):
        return self.username


class Job(models.Model):

    JOB_TYPE = (
        ("Full Time", "Full Time"),
        ("Part Time", "Part Time"),
        ("Internship", "Internship"),
        ("Contract", "Contract"),
    )

    WORK_MODE = (
        ("On Site", "On Site"),
        ("Hybrid", "Hybrid"),
        ("Remote", "Remote"),
    )

    EXPERIENCE = (
        ("Fresher", "Fresher"),
        ("0-1 Years", "0-1 Years"),
        ("1-3 Years", "1-3 Years"),
        ("3-5 Years", "3-5 Years"),
        ("5+ Years", "5+ Years"),
    )

    title = models.CharField(max_length=200)

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="jobs",
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posted_jobs",
    )

    description = models.TextField()

    responsibilities = models.TextField()

    requirements = models.TextField()

    location = models.CharField(max_length=150)

    salary = models.PositiveIntegerField()

    job_type = models.CharField(
        max_length=20,
        choices=JOB_TYPE,
    )

    work_mode = models.CharField(
        max_length=20,
        choices=WORK_MODE,
    )

    experience = models.CharField(
        max_length=20,
        choices=EXPERIENCE,
    )

    vacancy = models.PositiveIntegerField(default=1)

    application_deadline = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title