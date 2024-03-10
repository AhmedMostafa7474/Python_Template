from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from base.serializer import RoomSerializer, UserSerializer
from .models import Room
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from datetime import datetime

@method_decorator(csrf_exempt, name='dispatch')
class UserView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # Get the queryset for rooms hosted by 'ahmed'
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return JsonResponse({'users': serializer.data})


    
@method_decorator(csrf_exempt, name='dispatch')
class RoomView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # Get the queryset for rooms hosted by 'ahmed'
        queryset = Room.objects.all()
        serializer = RoomSerializer(queryset, many=True)
        return JsonResponse({'rooms': serializer.data})
    
    def post(self, request):
        room_name = request.POST.get('room_name', '')
        room = Room.objects.create(name=room_name, host=request.user)
        serializer = RoomSerializer(room)
        return JsonResponse({'room': serializer.data})
    
@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def post(self, request):
        username = request.GET.get('username', '')
        password = request.GET.get('password', '')
        print(username)
        try:
            user = User.objects.get(username=username)
        except:
            print("User Not Exist")
        userr = authenticate(request,username=username, password=password)
        if userr is not None:
            # login(request,user)
            token = AccessToken.for_user(user)
            expiration_time = datetime.fromtimestamp(token['exp'])
            return JsonResponse({'token': str(token), 'expiration_time': expiration_time})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
    
def home(request):
    queryset = Room.objects.filter(host__username='ahmed')
    
    for room in queryset:
        roomname = room.name
    return render(request,'home.html',{'username' :roomname})

def room(request,pk):
    return HttpResponse('Room Page')
