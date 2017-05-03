from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from models import StudentProfile, AdvisorProfile


# Used for advisor sign-up
class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)


class UserUpdateForm(forms.ModelForm):
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

class InviteAdvisorForm(forms.Form):
    advisor_name = forms.CharField(required=True)
    advisor_email = forms.EmailField(required=True)

# class SignUpForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password1', 'password2',)

"""
Forms for advisors
"""
# class AdvisorProfileForm(forms.ModelForm):
#   class Meta:
#       model = AdvisorProfile
#       fields = ('advisees',)
