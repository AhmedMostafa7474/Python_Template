from rest_framework import serializers
from .models import Owner, Room,RoomRequest,UserProfile,Chair
from django.contrib.auth.models import User



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['gender', 'city'] 
                
class UserSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    def get_gender(self, obj):
        try:
            return obj.profile.gender
        except:
            return ""
    def get_image(self, obj):
        try:
            return obj.profile.image.url
        except:
            return ""
    
        
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'email', 'gender','image', 'is_staff', 'is_active', 'last_login']


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['name']
        
        
class RequestSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(many=True)
    class Meta:
        model = RoomRequest
        fields = ['requester_name', 'price','type','owner']
        
class ChairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chair
        fields = ['name']
        
class RoomSerializer(serializers.ModelSerializer):
    host = UserSerializer()
    topic = serializers.CharField()
    requests = RequestSerializer(many=True, read_only=True)
    chairs =  serializers.SerializerMethodField()
    class Meta:
        model = Room
        fields = ['id', 'host', 'name', 'description', 'updated', 'created', 'topic','requests','chairs']

    def get_chairs(self, obj):
        return list(obj.chairs.values_list('name', flat=True))
    
