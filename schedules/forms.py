from django import forms
from models import Schedule, Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_id', 'course_name', 'area', 'overlay', 'credit', 'link', 'pre_req')

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('start_sem', 'end_sem', 'public')
