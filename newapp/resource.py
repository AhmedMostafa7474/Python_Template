from import_export import resources,fields
from .models import FormSubmission

class FormSubmissionResource(resources.ModelResource):
    image = fields.Field()
    class Meta:
         model = FormSubmission

    def dehydrate_image(self, mymodel):
        return "https://python.eyouthlearning.com" + mymodel.image.url
    