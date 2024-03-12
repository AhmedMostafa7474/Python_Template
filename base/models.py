from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Topic(models.Model):
      name = models.CharField(max_length=200)  
      def __str__(self):
        return self.name 
    
class Room(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True,blank=True)
    # participants
    
    def __str__(self):
        return self.name
    
class Chair(models.Model):
      room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='chairs')
      name = models.CharField(max_length=200)  
      def __str__(self):
        return self.name   
    
class RoomRequest(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='requests')
    requester_name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.requester_name
             
class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    body = models.TextField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body[0:50]
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    gender = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(null=True,blank=True,default="eyouth.png")
    # Add other additional fields as needed

    def __str__(self):
        return self.user.username