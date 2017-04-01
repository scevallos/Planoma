from django.contrib import admin

from .models import StudentProfile

# class StudentProfileAdmin(admin.ModelAdmin):
# 	list_display = ['user.first_name', 'user.last_name', 'year', 'dept']

admin.site.register(StudentProfile)