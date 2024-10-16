from django.shortcuts import render
from .models import ContactUS, CourseDeadline,FormSubmission, Lead, TrainerContactUS
from rest_framework import generics

# Create your views here.
from django.http import HttpResponse

from .serializer import ContactUsSerializer, CourseDeadlineSerializer, LeadSerializer, TrainerContactUsSerializer
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
        phonenumber = request.data.get('phonenumber','')
        userid = request.data.get('userid','')
        image = request.FILES.get('image')
        
        if username and email and code and image: 
            try:
                formsubmission = FormSubmission(username=username,email=email,codeid=code,image=image , phonenumber=phonenumber,userid=userid)
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
        
class ContactUSView(generics.CreateAPIView):
    serializer_class = ContactUsSerializer
    queryset = ContactUS.objects.all()
    
class TrainerContactUSView(generics.CreateAPIView):
    serializer_class = TrainerContactUsSerializer
    queryset = TrainerContactUS.objects.all()
    
class LeadView(generics.ListCreateAPIView):
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()
    
from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
import csv
from django.http import HttpResponse

def lead_list(request):
    # Search and filter functionality
    query = request.GET.get('query', '')
    campaign_filter = request.GET.get('campaign_name', '')
    
    leads = Lead.objects.all().order_by('-id')

    if query:
        leads = leads.filter(name__icontains=query) | leads.filter(email_id__icontains=query)
    
    if campaign_filter:
        leads = leads.filter(campaign_name=campaign_filter)

    # Pagination
    paginator = Paginator(leads, 20)  # Show 10 leads per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    total_leads = leads.count()

    # List of distinct campaign names for filter dropdown
    campaign_names = Lead.objects.values_list('campaign_name', flat=True).distinct()

    return render(request, 'lead_list.html', {
        'page_obj': page_obj,
        'campaign_names': campaign_names,
        'query': query,
        'selected_campaign': campaign_filter,
        'total_leads' : total_leads
    })

# CSV Download View
def download_csv(request):
    # Fetch all leads, or filter if needed
    leads = Lead.objects.all()

    # Filter based on search and campaign name
    query = request.GET.get('query', '')
    campaign_filter = request.GET.get('campaign_name', '')

    if query:
        leads = leads.filter(name__icontains=query) | leads.filter(email_id__icontains=query)
    
    if campaign_filter:
        leads = leads.filter(campaign_name=campaign_filter)

    # Prepare CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="leads.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['ID', 'Campaign Name', 'Name', 'Email', 'Mobile', 'UTM Source', 'Type', 'Created'])
    
    for lead in leads:
        writer.writerow([lead.id, lead.campaign_name, lead.name, lead.email_id, lead.mobile_no, lead.utm_source, lead.type, lead.created])
    
    return response

def lead_detail(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    return render(request, 'lead_detail.html', {'lead': lead})
