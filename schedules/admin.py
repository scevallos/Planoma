from django.contrib import admin

from .models import Schedule, Course, CourseSession

class ScheduleAdmin(admin.ModelAdmin):
	list_display = ['id', 'owner']

class CourseAdmin(admin.ModelAdmin):
	list_display = ['course_id', 'course_name']

class CourseSessionAdmin(admin.ModelAdmin):
	list_display = ['schedule', 'term', 'semester']

admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseSession, CourseSessionAdmin)
