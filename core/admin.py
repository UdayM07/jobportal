from django.contrib import admin
from .models import User,Company,Job,Application

from django.contrib.auth.admin import UserAdmin



@admin.register(User)
class CustomUserMOdel(admin.ModelAdmin):
    search_fields=['username']
    ordering=['username']
    list_filter=['is_active','is_staff','role']

@admin.register(Company)
class CustomCompanyModel(admin.ModelAdmin):
    list_display=['name','email','location']
    search_fields=['name']
    ordering=['name']



@admin.register(Job)
class CustomJobModel(admin.ModelAdmin):
    list_display=['title','company','location','salary','work_mode','work_mode','experience']
    search_fields=['title',"company"]
    ordering=['title',"company"]
    list_editable=['salary','work_mode']

@admin.register(Application)
class CustomApplication(admin.ModelAdmin):
    list_display=['job','candidate','applied_at']
    search_fields=['job', 'candidate']
    list_editable=['candidate']

    def job_created_by(self, obj):
        return obj.job.created_by


    
