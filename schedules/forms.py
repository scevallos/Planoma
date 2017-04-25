from django import forms
from models import Schedule, Course
from accounts.dept_codes import DEPTS
from constants import *

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_id', 'course_name', 'area', 'overlay', 'credit')

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('title', 'start_sem', 'end_sem', 'public', 'existing_credits', 'languages_completed', 'math_completed')


class ClassesTakenForm(forms.Form):
	classes_taken = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), widget=forms.CheckboxSelectMultiple())


# class ScheduleOptionsForm(forms.ModelForm):

	# existing_credits = forms.ChoiceField(choices = CREDIT_CHOICES,
	# 									 label = "Credits completed before college",
	# 									 initial = 'ZERO')

	# languages_completed = forms.ChoiceField(choices = LANGUAGE_CHOICES,
	# 										label = "Semesters of language taken",
	# 										initial = 'ZERO')

	# math_completed = forms.ChoiceField(choices = MATH_CHOICES,
	# 							       label = "Math completed before college",
	# 								   initial = 'NONE')

	# class Meta:
	# 	model = ScheduleOptions
	# 	fields = ('existing_credits', 'languages_completed', 'math_completed')


# class PreviousCourseForm(forms.ModelForm):
# 	department_selected = forms.ChoiceField(choices = DEPTS,
# 											default = 'CSCI')

# 	term_selected = forms.ChoiceField(choices = TERM_CHOICES,
# 									  default = 'SP17')

	