from django.urls import path
from . import views

urlpatterns = [
    path('deadlines/',views.CourseDeadlineView.as_view(),name="deadlines"),
    path('form',views.FormSubmissionView.as_view(),name="form"),
    path('sendmail/',views.SendEmailView.as_view(),name="email"),
    path('contactus/',views.ContactUSView.as_view(), name='ContactUSView'),
    path('trainercontactus/',views.TrainerContactUSView.as_view(), name='TrainerContactUSView'),
]