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
      username = models.CharField(max_length=200,null=True,blank=True)
      email = models.CharField(max_length=200,null=True,blank=True)
      codeid = models.CharField(max_length=200,null=True,blank=True)
      userid =  models.CharField(max_length=200,null=True,blank=True)
      phonenumber = models.CharField(max_length=200,null=True,blank=True)  
      image = models.ImageField(null=True,blank=True)
      updated = models.DateTimeField(auto_now=True)
      created = models.DateTimeField(auto_now_add=True)  
      def __str__(self):
        return self.username

from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$', 
    message="Phone number must be entered in correct format. Up to 15 digits allowed."
)

class TrainerContactUS(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone  = models.CharField(max_length=100,validators=[phone_regex])
    linked_in = models.URLField()
    message = models.TextField()
    def __str__(self):
        return f"{self.name}"

class ContactUS(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone  = models.CharField(max_length=100,validators=[phone_regex])
    message = models.TextField()
    def __str__(self):
        return f"{self.name}"