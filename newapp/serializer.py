from rest_framework import serializers
from .models import CourseDeadline



class CourseDeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDeadline
        fields = ['username', 'coursekey','deadline'] 
                