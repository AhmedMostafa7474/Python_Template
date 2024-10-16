from django.urls import path
from . import views

urlpatterns = [
    path('deadlines/',views.CourseDeadlineView.as_view(),name="deadlines"),
    path('form',views.FormSubmissionView.as_view(),name="form"),
    path('sendmail/',views.SendEmailView.as_view(),name="email"),
    path('contactus/',views.ContactUSView.as_view(), name='ContactUSView'),
    path('trainercontactus/',views.TrainerContactUSView.as_view(), name='TrainerContactUSView'),
    path('lead/',views.LeadView.as_view(), name='lead'),
    path('leads/', views.lead_list, name='lead_list'),
    path('leads/<int:pk>/', views.lead_detail, name='lead_detail'),
    path('leads/download/', views.download_csv, name='download_csv'),

]