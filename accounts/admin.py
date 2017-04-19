from django.contrib import admin

from .models import StudentProfile, AdvisorProfile

class StudentProfileAdmin(admin.ModelAdmin):
	fields = ['user.first_name', 'user.last_name', 'year', 'dept']

admin.site.register(StudentProfile, StudentProfileAdmin)
admin.site.register(AdvisorProfile)