from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User,Company,Job
from django.contrib.auth.forms import AuthenticationForm


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

    def clean(self):
     cleaned_data = super().clean()

     role = cleaned_data.get("role")
     company = cleaned_data.get("company")

     if role == "Recruiter" and not company:
        raise forms.ValidationError({
            "company": "Choose a company."
        })

     if role == "Candidate" and company:
        raise forms.ValidationError({
            "company": "Candidates cannot choose a company."
        })

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
                "class": "w-full rounded-xl border border-gray-300 px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            })

        self.fields["title"].widget.attrs["placeholder"] = "Python Django Developer"
        self.fields["location"].widget.attrs["placeholder"] = "Bengaluru"
        self.fields["salary"].widget.attrs["placeholder"] = "600000"
        self.fields["vacancy"].widget.attrs["placeholder"] = "5"

        self.fields["description"].widget.attrs["placeholder"] = "Enter job description..."
        self.fields["responsibilities"].widget.attrs["placeholder"] = "List job responsibilities..."
        self.fields["requirements"].widget.attrs["placeholder"] = "Required skills and qualifications..."


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        exclude = ("created_at",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "w-full rounded-xl border border-gray-300 px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            })

        self.fields["name"].widget.attrs["placeholder"] = "Company Name"
        self.fields["website"].widget.attrs["placeholder"] = "https://company.com"
        self.fields["email"].widget.attrs["placeholder"] = "Company Email"
        self.fields["phone"].widget.attrs["placeholder"] = "Phone Number"
        self.fields["location"].widget.attrs["placeholder"] = "Company Location"
        self.fields["description"].widget.attrs["placeholder"] = "Write about your company..."