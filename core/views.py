from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm, JobForm
from .models import Job, Application


# ---------------- Register ----------------

def register(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Registration successful. Please login."
            )

            return redirect("login")

    else:
        form = RegisterForm()

    return render(
        request,
        "core/register.html",
        {
            "form": form
        }
    )


# ---------------- Login ----------------

def login_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        form = LoginForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            login(
                request,
                form.get_user()
            )

            return redirect("home")

    else:
        form = LoginForm(request)

    return render(
        request,
        "core/login.html",
        {
            "form": form
        }
    )


# ---------------- Logout ----------------

@login_required
def logout_view(request):

    logout(request)

    return redirect("login")



def home(request):

    jobs = Job.objects.order_by("-created_at")

    if request.user.is_authenticated:

        if request.user.role == "Recruiter":

            jobs = jobs.exclude(
                created_by=request.user
            )

    jobs=jobs[:3]

    return render(
        request,
        "core/home.html",
        {
            "jobs": jobs
        }
    )




@login_required
def create_job(request):

    if request.user.role != "Recruiter":
        return redirect("home")

    if request.method == "POST":

        form = JobForm(request.POST)

        if form.is_valid():

            job = form.save(commit=False)

            job.created_by = request.user

            job.company = request.user.company

            job.save()

            messages.success(
                request,
                "Job posted successfully."
            )

            return redirect("profile")

    else:

        form = JobForm()

    return render(
        request,
        "core/job_form.html",
        {
            "form": form
        }
    )




def job_detail(request, pk):

    job = get_object_or_404(
        Job,
        pk=pk
    )

    

    if (
        request.user.is_authenticated and
        request.user.role == "Candidate"
    ):

        already_applied = Application.objects.filter(
            job=job,
            candidate=request.user
        ).exists()

    return render(
        request,
        "core/job_detail.html",
        {
            "job": job,
            
        }
    )




def list_jobs(request):

    jobs = Job.objects.order_by("-created_at")

    search = request.GET.get("search")

    if search:

        jobs = jobs.filter(

            Q(title__icontains=search) |
            Q(company__icontains=search)

        )

    location = request.GET.get("location")

    if location:

        jobs = jobs.filter(
            location__icontains=location
        )

    job_type = request.GET.get("job_type")

    if job_type:

        jobs = jobs.filter(
            job_type=job_type
        )

    work_mode = request.GET.get("work_mode")

    if work_mode:

        jobs = jobs.filter(
            work_mode=work_mode
        )

    experience = request.GET.get("experience")

    if experience:

        jobs = jobs.filter(
            experience=experience
        )

    paginator = Paginator(
        jobs,
        6
    )

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(
        page_number
    )

    return render(
        request,
        "core/job_list.html",
        {
            "jobs": page_obj
        }
    )


# ---------------- Edit Job ----------------

@login_required
def edit_view(request, pk):

    if request.user.role != "Recruiter":
        return redirect("home")

    job = get_object_or_404(
        Job,
        pk=pk,
        created_by=request.user
    )

    if request.method == "POST":

        form = JobForm(
            request.POST,
            instance=job
        )

        if form.is_valid():

            edited_job = form.save(commit=False)

            edited_job.company = request.user.company

            edited_job.created_by = request.user

            edited_job.save()

            messages.success(
                request,
                "Job updated successfully."
            )

            return redirect("profile")

    else:

        form = JobForm(
            instance=job
        )

    return render(
        request,
        "core/job_form.html",
        {
            "form": form
        }
    )


# ---------------- Delete Job ----------------

@login_required
def delete_view(request, pk):

    if request.user.role != "Recruiter":
        return redirect("home")

    job = get_object_or_404(
        Job,
        pk=pk,
        created_by=request.user,
    )

    job.delete()

    messages.success(
        request,
        "Job deleted successfully."
    )

    return redirect("profile")


# ---------------- Recruiter Profile ----------------

@login_required
def Profile(request):

    

    jobs = Job.objects.filter(
        created_by=request.user
    ).order_by("-created_at")

    context = {
        "jobs": jobs,
        "job_count": jobs.count(),
    }

    return render(
        request,
        "core/profile.html",
        context,
    )


# ---------------- Apply Job ----------------

@login_required
def apply_job(request, pk):

    if request.user.role != "Candidate":
        return redirect("home")

    job = get_object_or_404(
        Job,
        pk=pk,
    )

    if Application.objects.filter(
        job=job,
        candidate=request.user,
    ).exists():

        messages.warning(
            request,
            "You have already applied for this job."
        )

        return redirect("job_detail", pk=pk)

    Application.objects.create(
        job=job,
        candidate=request.user,
    )

    messages.success(
        request,
        "Application submitted successfully."
    )

    return redirect("my_applications")



@login_required
def my_applications(request):

    if request.user.role != "Candidate":
        return redirect("home")

    applications = (
        Application.objects
        .filter(candidate=request.user)
        
        .order_by("-applied_at")
    )

    context = {
        "applications": applications,
    }

    return render(
        request,
        "core/application.html",
        context,
    )


# ---------------- View Applicants ----------------
@login_required
def applicants(request, pk):

    job = get_object_or_404(
        Job,
        pk=pk,
        created_by=request.user
    )

    applications = Application.objects.filter(
        job=job
    )

    context = {
        "job": job,
        "applications": applications,
    }

    return render(request, "core/applicants.html", context)