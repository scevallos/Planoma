from django.contrib import admin

from .models import Schedule, Course, CourseSession

class ScheduleAdmin(admin.ModelAdmin):
	list_display = ['id', 'owner']

admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Course)
admin.site.register(CourseSession)
