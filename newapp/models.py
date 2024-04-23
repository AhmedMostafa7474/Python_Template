from django.db import models

# Create your models here.
class CourseDeadline(models.Model):
      username = models.CharField(max_length=200)
      coursekey = models.CharField(max_length=200)  
      deadline = models.CharField(max_length=200)    
      updated = models.DateTimeField(auto_now=True)
      created = models.DateTimeField(auto_now_add=True)  
      def __str__(self):
        return self.username + " " + self.coursekey
      
class FormSubmission(models.Model):
      username = models.CharField(max_length=200)
      email = models.CharField(max_length=200)
      codeid = models.CharField(max_length=200)  
      image = models.ImageField(null=True,blank=True)
      updated = models.DateTimeField(auto_now=True)
      created = models.DateTimeField(auto_now_add=True)  
      def __str__(self):
        return self.username