from django.urls import path
from .import views

urlpatterns = [
    path("register/",views.register,name='register'),
    path("login/",views.login_view,name='login'),
    path("logout/",views.logout_view,name='logout'),
    path("",views.home,name='home'),
    path("create_job/",views.create_job,name='job_form'),
    path("job_detail/<int:pk>/",views.job_detail,name='job_detail'),
    path("list_jobs/",views.list_jobs,name='list_jobs'),
    path("edit/<int:pk>/",views.edit_view,name='edit'),
    path("delete/<int:pk>/",views.delete_view,name='delete'),
    path("Profile/",views.Profile,name='profile'),
    path("apply_job/<int:pk>/",views.apply_job,name='apply_job'),
    path("my-applications/", views.my_applications, name="my_applications"),
    path("applicants/<int:pk>/", views.applicants, name="applicants"),

    

   
    
    

]
