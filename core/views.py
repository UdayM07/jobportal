from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegisterForm,LoginForm,JobForm
from django.contrib.auth import login,logout
from .models import Company,Job,Application
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages



# Create your views here.

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=RegisterForm()
    return render(request,'core/register.html',{'form':form})


def login_view(request):
    if request.method=='POST':
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        form=LoginForm(request)

            
    return render(request,'core/login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')


def home(request):
    jobs=Job.objects.exclude(created_by=request.user).order_by('-created_at')[:3]
   

    context={'jobs':jobs}
    return render(request,'core/home.html',context)



def create_job(request):
    if request.user.role!="Recruiter":
        return redirect('home')
    if request.method=="POST":
        form=JobForm(request.POST)
        if form.is_valid():
           job= form.save(commit=False)
           job.created_by=request.user
           job.company=request.user.company
           job.save()
           return redirect('home')
    else:
        form=JobForm()

    context={'form':form}
    return render(request,'core/job_form.html',context)


def job_detail(request,pk):
    job=get_object_or_404(Job,pk=pk)
    context={'job':job}
    return render(request,'core/job_detail.html',context)

def list_jobs(request):
    jobs=Job.objects.all()
    search=request.GET.get('search')
    if search:
        jobs=jobs.filter(
            Q(title__icontains=search)|
            Q(company__name__icontains=search)
        )
    location=request.GET.get('location')
    if location:
        jobs = jobs.filter(
            location__icontains=location
        )

    job_type = request.GET.get("job_type")

    if job_type:
        jobs = jobs.filter(job_type=job_type)

    work_mode = request.GET.get("work_mode")

    if work_mode:
            jobs = jobs.filter(work_mode=work_mode)

    experience = request.GET.get("experience")
    if experience:
        jobs=jobs.filter(experience=experience)
        print(request.GET)

    paginator = Paginator(jobs, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number) 

      

    

    

    context={
        'jobs':page_obj
    }
    return render(request,'core/job_list.html',context)



def edit_view(request,pk):
    print("EDIT VIEW CALLED")
    if request.user.role!="Recruiter":
        return redirect('home')
    job=get_object_or_404(Job,pk=pk,created_by=request.user)
    if request.method=='POST':
        form=JobForm(request.POST,instance=job)
        if form.is_valid():
            form.save()
            return redirect ('home')
    else:
        form=JobForm(instance=job)
    context={
        'form':form
    }
    return render(request,'core/job_form.html',context)

def delete_view(request,pk):
    if request.user.role!="Recruiter":
        return redirect('home')
    job=get_object_or_404(Job,pk=pk)
    job.delete()
    return redirect('home')

    

        
                
def Profile(request):

    jobs = Job.objects.filter(
        created_by=request.user
    ).order_by("-created_at")

    context = {
        "jobs": jobs,
        "job_count": jobs.count(),
    }

    return render(request, "core/profile.html", context)


def apply_job(request, pk):
    job = get_object_or_404(Job, pk=pk)

    if not request.user.is_authenticated:
        return redirect("login")

    if request.user.role != "Candidate":
        return redirect("home")

    if Application.objects.filter(
        job=job,
        candidate=request.user
    ).exists():
        messages.warning(request,'you have already applied for this job')
        return redirect("home")

    Application.objects.create(
        job=job,
        candidate=request.user
    )

    messages.success(request, "Application submitted successfully.")
    return redirect("list_jobs")


def my_applications(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.role!='Candidate':
        return redirect('home')
    applications=Application.objects.filter(candidate=request.user)
    context={
        'applications':applications
    }
    return render(request,'core/application.html',context)

def applicants(request,pk):
    if not request.user.is_authenticated:
        return redirect('login')    
    if request.user.role!='Recruiter':
        return redirect('home')
    selected_job=get_object_or_404(Job,pk=pk,created_by=request.user)
    
    applications=Application.objects.filter(
        job=selected_job,
    )
    context={
        'applications':applications,
        'job':selected_job

    }   
    return render(request,'core/applicants.html',context)
   
   
    








    













    





