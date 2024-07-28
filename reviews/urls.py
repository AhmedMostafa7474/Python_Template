from django.urls import path
from . import views

urlpatterns = [
    path('',views.SurveyListCreate.as_view(),name="survay-create"),
    path('checksurvey/',views.SurvayValidationView.as_view(),name="survay-create"),
    path('basketchecksurvey/',views.SurvayBasketValidationView.as_view(),name="survay-basket"),

]