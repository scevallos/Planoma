from django import forms
from models import Schedule, Course
from planoma.accounts.dept_codes import DEPTS
from planoma.schedules.schedule_options import *

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_id', 'course_name', 'area', 'overlay', 'credit', 'link', 'pre_req')

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('title', 'start_sem', 'end_sem', 'public')


class ScheduleOptionsForm(forms.ModelForm):

	existing_credits = forms.ChoiceField(choices = CREDIT_CHOICES,
										 label = "Credits completed before college",
										 default = 'ZERO')

	languages_completed = forms.ChoiceField(choices = LANGUAGE_CHOICES,
											label = "Semesters of language taken",
											default = 'ZERO')

	math_completed = forms.ChoiceField(choices = MATH_CHOICES,
								       label = "Math completed before college",
									   default = 'NONE')

	class Meta:
		model = ScheduleOptions


# class PreviousCourseForm(forms.ModelForm):
# 	department_selected = forms.ChoiceField(choices = DEPTS,
# 											default = 'CSCI')

# 	term_selected = forms.ChoiceField(choices = TERM_CHOICES,
# 									  default = 'SP17')

	