from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import format_html
# Register your models here.
from .models import Room,Topic,Message,RoomRequest,UserProfile,Chair
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

class RoomAdmin(admin.ModelAdmin):
    search_fields = ['host__username','name']
    list_display = ('name', 'host')
    list_filter = ('host',)
    def view_link(self, obj):
        return format_html('<a href="{}">{}</a>', f"http://www.google.com/{obj.name}", obj.name)
    view_link.short_description = "View Link"  
    
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Room,RoomAdmin)
admin.site.register(Chair)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(RoomRequest)