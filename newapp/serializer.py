from rest_framework import serializers
from .models import ContactUS, CourseDeadline, Lead, TrainerContactUS



class CourseDeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDeadline
        fields = ['username', 'coursekey','deadline'] 
        
class ContactUsSerializer(serializers.ModelSerializer):
      class Meta:
            model = ContactUS
            fields = '__all__'

class TrainerContactUsSerializer(serializers.ModelSerializer):
      class Meta:
            model = TrainerContactUS
            fields = '__all__'
            
class LeadSerializer(serializers.ModelSerializer):
      class Meta:
            model = Lead
            fields = '__all__'