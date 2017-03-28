# from django import forms
# from django.contrib.auth.models import User
# from models import Profile

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('dept',)


from django import forms
from django.contrib.auth.models import User
from models import Profile


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
        fields = ('major', 'year')

## A form to be used by students to invite their advisors
class AdvisorInviteForm(forms.ModelForm):
	class Meta:
		model = AdvisorProfile
		fields = ('dept','email')


"""
Forms for advisors
"""
class AdvisorProfileForm(forms.ModelForm):
	class Meta:
		model = AdvisorProfile
		fields = ('advisees')