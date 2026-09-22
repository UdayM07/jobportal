from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User, Job


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "company",
            "role",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "w-full rounded-xl border border-gray-300 px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
            })

        self.fields["username"].widget.attrs["placeholder"] = "Username"
        self.fields["first_name"].widget.attrs["placeholder"] = "First Name"
        self.fields["last_name"].widget.attrs["placeholder"] = "Last Name"
        self.fields["email"].widget.attrs["placeholder"] = "Email Address"
        self.fields["company"].widget.attrs["placeholder"] = "Company Name"

    def clean(self):
        cleaned_data = super().clean()

        role = cleaned_data.get("role")
        company = cleaned_data.get("company")

        if role == "Recruiter" and not company:
            self.add_error(
                "company",
                "Company name is required for recruiters."
            )

        if role == "Candidate":
            cleaned_data["company"] = ""

        return cleaned_data


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "w-full rounded-xl border border-gray-300 px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
            })

        self.fields["username"].widget.attrs["placeholder"] = "Enter Username"
        self.fields["password"].widget.attrs["placeholder"] = "Enter Password"


class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        exclude = (
            "company",
            "created_by",
            "created_at",
            "updated_at",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "w-full rounded-xl border border-gray-300 px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
            })

        self.fields["title"].widget.attrs["placeholder"] = "Python Django Developer"
        self.fields["location"].widget.attrs["placeholder"] = "Bengaluru"
        self.fields["salary"].widget.attrs["placeholder"] = "600000"
        self.fields["vacancy"].widget.attrs["placeholder"] = "5"

        self.fields["description"].widget.attrs["placeholder"] = "Enter job description..."
        self.fields["responsibilities"].widget.attrs["placeholder"] = "List job responsibilities..."
        self.fields["requirements"].widget.attrs["placeholder"] = "Required skills and qualifications..."