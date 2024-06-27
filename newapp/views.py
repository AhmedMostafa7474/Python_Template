from django.shortcuts import render
from .models import CourseDeadline,FormSubmission

# Create your views here.
from django.http import HttpResponse

from .serializer import CourseDeadlineSerializer
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings

@method_decorator(csrf_exempt, name='dispatch')
class CourseDeadlineView(APIView):
    
    def get(self, request):
        username = request.GET.get('username')
        queryset = CourseDeadline.objects.filter(username=username)
        serializer = CourseDeadlineSerializer(queryset, many=True)
        return JsonResponse({'Deadlines': serializer.data})
    def post(self,request):
        users = request.data.get('users')
        courses = request.data.get('courses')
        deadline = request.data.get('deadline')
        
        if users and courses and deadline: 
            try:
                course_deadlines = []
                for user in users:
                    for course in courses:
                        course_deadlines.append(CourseDeadline(username=user, coursekey=course, deadline=deadline))
                
                CourseDeadline.objects.bulk_create(course_deadlines)

            except Exception as e:
                    print("Error occurred while creating CourseDeadline records:" + e)
                    return JsonResponse({'error': 'Error happened while creating records '}, status=500)

            return JsonResponse({"message": "Deadlines created successfully"})
        else:
            return JsonResponse({'error': 'Invalid Input, Missing data'}, status=400)
        
        
class FormSubmissionView(APIView):
    def post(self,request):
        username = request.data.get('username')
        email = request.data.get('email')
        code = request.data.get('code')
        phonenumber = request.data.get('phonenumber')
        image = request.FILES.get('image')
        
        if username and email and code and image and phonenumber: 
            try:
                formsubmission = FormSubmission(username=username,email=email,codeid=code,image=image , phonenumber=phonenumber)
                formsubmission.save()
            except Exception as e:
                    return JsonResponse({'error': 'Error happened while creating records ' + str(e)}, status=500)

            return JsonResponse({"message": "Form Submission created successfully"})
        else:
            return JsonResponse({'error': 'Invalid Input, Missing data'}, status=400)
        

    
@method_decorator(csrf_exempt, name='dispatch')
class SendEmailView(APIView):
    def send_test_email(self):
        subject = 'Test Email'
        message = 'This is a test email sent from Django.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['kudo7474@gmail.com']
        send_mail(subject, message, email_from, recipient_list)

    def post(self,request):
        try:
            self.send_test_email()
            return JsonResponse({"message": "Email Sent successfully"})
            
        except Exception as e:
            print(f"Email sending failed: {e}")
            return JsonResponse({'error': 'Email Failed '+str(e)}, status=400)