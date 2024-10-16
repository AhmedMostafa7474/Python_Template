from django.contrib import admin
from .models import CourseDeadline,FormSubmission,ContactUS, Lead,TrainerContactUS
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
    
class LeadAdmin(ImportExportModelAdmin):
    search_fields = ['name','email_id']
    list_display = ('name', 'email_id','mobile_no','campaign_name','created')   
    list_filter = ['campaign_name']
# admin.site.register(CourseDeadline)
admin.site.register(FormSubmission,FormSubmissionAdmin)
admin.site.register(ContactUS,ContactUSAdmin)
admin.site.register(TrainerContactUS,TrainerContactUSAdmin)
admin.site.register(Lead,LeadAdmin)