from django.urls import path
from . import views

urlpatterns = [
    path('deadlines/',views.CourseDeadlineView.as_view(),name="deadlines"),
]