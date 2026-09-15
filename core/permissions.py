from rest_framework.permissions import BasePermission

class IsRecruiter(BasePermission):
    def has_permission(self,request,view):
     if request.method in ['GET','OPTIONS','HEAD']:
        return True
     return (
      request.user.is_authenticated
       and (
        request.user.is_superuser
        or request.user.role == "Recruiter"
    )
)

    

    def has_object_permission(self,request,view,obj):
       if request.method in ['GET','OPTIONS','HEAD']:
          return True 
       else:
          return (
             obj.created_by==request.user or request.user.is_superuser
          )


          


