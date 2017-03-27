from django.contrib import admin

from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'full_name', 'year' ,'email']

admin.site.register(UserProfile, UserProfileAdmin)