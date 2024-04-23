from django.contrib import admin
from .models import CourseDeadline,FormSubmission
# Register your models here.

class FormSubmissionAdmin(admin.ModelAdmin):
    search_fields = ['username','email']
    list_display = ('username', 'email' ,'codeid','image')
admin.site.register(CourseDeadline)
admin.site.register(FormSubmission,FormSubmissionAdmin)
