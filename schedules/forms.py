from django import forms
from models import Schedule, Course, CourseSession
from accounts.dept_codes import DEPTS
from constants import *

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_id', 'course_name', 'area', 'overlay', 'credit')

class TermForm(forms.ModelForm):
    class Meta:
        model = CourseSession
        fields = ('term', 'semester')

class ScheduleForm(forms.ModelForm):
    classes_taken = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Schedule
        # Make dummy course sessions with previous courses
        fields = ('title', 'start_sem', 'end_sem', 'public', 'existing_credits', 'languages_completed', 'math_completed')

class AddTermForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.sessions = kwargs.pop('sessions')
        self.courses = kwargs.pop('courses')
        super(AddTermForm, self).__init__(*args, **kwargs)
        self.fields['terms'].queryset = self.sessions

    terms = forms.ModelChoiceField(queryset=Course.objects.none())

class firstYearForm(forms.ModelForm):
    """docstring for firstYearForm"""
    class Meta:
        model = Schedule
        fields = ('title', 'start_sem', 'end_sem', 'public', 'existing_credits',
            'languages_completed', 'math_completed')



# class ScheduleOptionsForm(forms.ModelForm):

    # existing_credits = forms.ChoiceField(choices = CREDIT_CHOICES,
    #                                    label = "Credits completed before college",
    #                                    initial = 'ZERO')

    # languages_completed = forms.ChoiceField(choices = LANGUAGE_CHOICES,
    #                                       label = "Semesters of language taken",
    #                                       initial = 'ZERO')

    # math_completed = forms.ChoiceField(choices = MATH_CHOICES,
    #                                  label = "Math completed before college",
    #                                  initial = 'NONE')

    # class Meta:
    #   model = ScheduleOptions
    #   fields = ('existing_credits', 'languages_completed', 'math_completed')


# class PreviousCourseForm(forms.ModelForm):
#   department_selected = forms.ChoiceField(choices = DEPTS,
#                                           default = 'CSCI')

#   term_selected = forms.ChoiceField(choices = TERM_CHOICES,
#                                     default = 'SP17')
