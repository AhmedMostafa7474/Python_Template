from django.contrib import admin

from reviews.models import Survey
from import_export.admin import ImportExportModelAdmin

from reviews.resource import SurveyResource

# Register your models here.
class SurveyAdmin(ImportExportModelAdmin):
     resource_class = SurveyResource      
     filter_horizontal = ('categories',)
     
admin.site.register(Survey,SurveyAdmin)
