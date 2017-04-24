from django import forms
from django.contrib.auth.models import User
from models import StudentProfile, AdvisorProfile


"""
Forms for students
"""

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


# Seen on the profile page
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ('dept', 'year')



## A form to be used by students to invite their advisors
class AdvisorInviteForm(forms.ModelForm):
	class Meta:
		model = AdvisorProfile
		fields = ('dept',)


"""
Forms for advisors
"""
# class AdvisorProfileForm(forms.ModelForm):
# 	class Meta:
# 		model = AdvisorProfile
# 		fields = ('advisees',)