from rest_framework import serializers

from .models import Job, User, Application


# ---------------- Job Serializer ----------------

class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = "__all__"
        read_only_fields = (
            "company",
            "created_by",
            "created_at",
            "updated_at",
        )


# ---------------- Register Serializer ----------------

class RegisterSerializer(serializers.ModelSerializer):

    password1 = serializers.CharField(
        write_only=True,
        min_length=8,
    )

    password2 = serializers.CharField(
        write_only=True,
        min_length=8,
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "role",
            "company",
            "password1",
            "password2",
        ]

    def validate(self, attrs):

        password1 = attrs.get("password1")
        password2 = attrs.get("password2")

        role = attrs.get("role")
        company = attrs.get("company", "").strip()

        if password1 != password2:
            raise serializers.ValidationError({
                "password2": "Passwords do not match."
            })

        if role == "Recruiter" and not company:
            raise serializers.ValidationError({
                "company": "Company name is required for recruiters."
            })

        if role == "Candidate":
            attrs["company"] = ""

        if not any(ch.isupper() for ch in password1):
            raise serializers.ValidationError({
                "password1": "Password must contain at least one uppercase letter."
            })

        return attrs

    def create(self, validated_data):

        password = validated_data.pop("password1")
        validated_data.pop("password2")

        return User.objects.create_user(
            password=password,
            **validated_data
        )


# ---------------- Application Serializer ----------------

class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = "__all__"
        read_only_fields = (
            "job",
            "candidate",
            "applied_at",
        )