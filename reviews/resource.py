from import_export import resources,fields
from .models import Survey

class SurveyResource(resources.ModelResource):
    categories = fields.Field()
    class Meta:
         model = Survey
    
    def get_export_headers(self):
        headers = []
        for field in self.get_export_fields():
            if isinstance(field, fields.Field):
                field_name = field.attribute
            else:
                field_name = field
            if field_name == None:
                field_name = "categories"
            field = self.Meta.model._meta.get_field(field_name)
            if field.verbose_name:
                    verbose_name = field.verbose_name
            else:
                    verbose_name = field_name
            headers.append(verbose_name)
        return headers
    
    def dehydrate_categories(self, mymodel):
        return ', '.join([category.title for category in mymodel.categories.all()])