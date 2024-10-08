from django.contrib import admin
from .models import CourseDeadline,FormSubmission,ContactUS,TrainerContactUS
from .resource import FormSubmissionResource  
from import_export.admin import ImportExportModelAdmin

class FormSubmissionAdmin(ImportExportModelAdmin):
    resource_class = FormSubmissionResource      
    search_fields = ['username','email']
    list_display = ('username', 'email','phonenumber','codeid','userid','image')
    
class ContactUSAdmin(ImportExportModelAdmin):
    search_fields = ['name','email']
    list_display = ('name', 'email','phone','message')

class TrainerContactUSAdmin(ImportExportModelAdmin):
    search_fields = ['name','email']
    list_display = ('name', 'email','phone','message')   
# admin.site.register(CourseDeadline)
admin.site.register(FormSubmission,FormSubmissionAdmin)
admin.site.register(ContactUS,ContactUSAdmin)
admin.site.register(TrainerContactUS,TrainerContactUSAdmin)