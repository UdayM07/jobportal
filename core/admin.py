from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Job, Application


# ---------------- User ----------------

@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        "id",
        "username",
        "email",
        "role",
        "company",
        "is_active",
        "is_staff",
    )

    search_fields = (
        "username",
        "email",
        "company",
    )

    ordering = (
        "username",
    )

    list_filter = (
        "role",
        "is_active",
        "is_staff",
    )


# ---------------- Job ----------------

@admin.register(Job)
class CustomJobAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "company",
        "created_by",
        "location",
        "salary",
        "job_type",
        "work_mode",
        "experience",
        "created_at",
    )

    search_fields = (
        "title",
        "company",
        "created_by__username",
    )

    list_filter = (
        "job_type",
        "work_mode",
        "experience",
    )

    ordering = (
        "-created_at",
    )

    list_editable = (
        "salary",
        "work_mode",
    )


# ---------------- Application ----------------

@admin.register(Application)
class CustomApplicationAdmin(admin.ModelAdmin):

    list_display = (
        "job",
        "candidate",
        "applied_at",
    )

    search_fields = (
        "job__title",
        "candidate__username",
    )

    ordering = (
        "-applied_at",
    )