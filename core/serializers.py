from rest_framework import serializers
from .models import Job, User,Application



# ---------------- Job Serializer ----------------
class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = "__all__"
        read_only_fields = [
            "created_by",
            "created_at",
            "updated_at",
        ]


# ---------------- Register Serializer ----------------
class RegisterSerializer(serializers.ModelSerializer):

    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

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

        if attrs["password1"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password2": "Passwords do not match."}
            )

        if attrs["role"] == "Recruiter" and not attrs.get("company"):
            raise serializers.ValidationError(
                {"company": "Choose a company if you are a Recruiter."}
            )

        if attrs["role"] == "Candidate" and attrs.get("company"):
            raise serializers.ValidationError(
                {"company": "Candidates cannot choose a company."}
            )

        if len(attrs["password1"]) < 8:
            raise serializers.ValidationError(
                {"password1": "Password must contain at least 8 characters."}
            )

        has_upper = False

        for ch in attrs["password1"]:
            if ch.isupper():
                has_upper = True
                break

        if not has_upper:
            raise serializers.ValidationError(
                {
                    "password1": "Password must contain at least one uppercase letter."
                }
            )

        return attrs

    def create(self, validated_data):

        password = validated_data.pop("password1")
        validated_data.pop("password2")

        user = User.objects.create_user(
            password=password,
            **validated_data
        )

        return user

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Application 
        fields='__all__'
        read_only_fields = ["job", "candidate", "applied_at"]
