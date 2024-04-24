from django.contrib import admin
from .models import CourseDeadline,FormSubmission
from .resource import FormSubmissionResource  
from import_export.admin import ImportExportModelAdmin

class FormSubmissionAdmin(ImportExportModelAdmin):
    resource_class = FormSubmissionResource      
    search_fields = ['username','email']
    list_display = ('username', 'email' ,'codeid','image')

admin.site.register(CourseDeadline)
admin.site.register(FormSubmission,FormSubmissionAdmin)
