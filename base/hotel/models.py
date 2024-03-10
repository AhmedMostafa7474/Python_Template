from django.db import models
# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=200)  
    address = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.name 
    