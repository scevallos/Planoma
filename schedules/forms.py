from django import forms
from models import Schedule, Course
from accounts.dept_codes import DEPTS

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_id', 'course_name', 'area', 'overlay', 'credit', 'link', 'pre_req')

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('title', 'start_sem', 'end_sem', 'public')

# class CreditsForm(forms.ModelForm):
#     CREDIT_CHOICES = (
#         ('0', '0'),
#         ('1',  '1'),
#         ('2',  '2'), 
#     )

#     credits_completed = forms.ChoiceField(choices = CREDIT_CHOICES,
#                                           default = '0')

# class LanguageForm(forms.ModelForm):
#     LANGUAGE_CHOICES = (
#         ('0',  '0'),
#         ('1',   '1'),
#         ('2',   '2'),
#         ('3', '3'),
#     )

#     languages_completed = forms.ChoiceField(choices = LANGUAGE_CHOICES,
#                                             default = '0')

# class PreviousCourseForm(forms.ModelForm):
#     department_selected = forms.ChoiceField(choices = DEPTS,
#                                             default = CSCI)

#     TERM_CHOICES = (
#         ('FA13', 'Fall 2013'),
#         ('SP14', 'Spring 2014'),
#         ('FA14', 'Fall 2014'),
#         ('SP15', 'Spring 2015'),
#         ('FA15', 'Fall 2015'),
#         ('SP16', 'Spring 2016'),
#         ('FA16', 'Fall 2016'),
#         ('SP17', 'Spring 2017'),
#     )

#     term_selected = forms.ChoiceField(choices = TERM_CHOICES,
#                                       default = 'FA13')



# class MathForm(forms.ModelForm):
#     MATH_CHOICES = (
#         ('None', 'None'),
#         ('CALC1', 'Calc I'),
#         ('CALC2', 'Calc II'),
#         ('LINEAR', 'Linear +')
#     )

#     math_completed = forms.ChoiceField(choices = MATH_CHOICES,
#                                        default = 'None')