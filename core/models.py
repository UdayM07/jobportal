from django.db import models
from django.contrib.auth.models import AbstractUser


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

    company = models.CharField(
        max_length=100,
        blank=True,
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

    company = models.CharField(
        max_length=100,
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


class Application(models.Model):

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
    )

    candidate = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    applied_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        unique_together = ("job", "candidate")