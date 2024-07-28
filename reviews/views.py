from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status,mixins
from rest_framework.response import Response

from reviews.serialziers import SurveySerializer
from .models import Survey

class SurveyListCreate(mixins.UpdateModelMixin,generics.ListCreateAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        if username:
            try:
                existing_survey = Survey.objects.get(username=username)
                serializer = self.get_serializer(existing_survey, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Survey.DoesNotExist:
                pass
        
        return super().create(request, *args, **kwargs)

class SurvayValidationView(generics.ListCreateAPIView):
    def getenrolment_status(self,username):
        import requests

        url = "https://experience.eyouthlearning.com/api/courses/v1/checksurvey/?username=" + username

        payload = ""
        headers = {
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        json_response = response.json()

        need_survey = json_response.get('need_survey')
        print ("need_survay: ", need_survey)
        return need_survey

    def get(self, request):
        try:
            username = request.GET.get('username')
            existing_survey = Survey.objects.get(username=username)
            status = existing_survey.completed
            if status:
                return JsonResponse({"need_survey":"false"}, safe=False)
            else:
                return JsonResponse({"need_survey":"true"}, safe=False)

        except Survey.DoesNotExist:
            if self.getenrolment_status(username):
                return JsonResponse({"need_survey":"true"}, safe=False)
            else:
                return JsonResponse({"need_survey":"false"}, safe=False)

