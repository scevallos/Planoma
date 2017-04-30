# from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.template import loader
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group

from models import StudentProfile
from schedules.models import Schedule, Course, CourseSession
from forms import UserForm, StudentProfileForm, InviteAdvisorForm
from group_decorator import *
from invitations.models import *


def index(request):
    return render(request, 'index.html',)

def contact_us(request):
    return render(request, 'contact-us.html',)

@login_required
def profile_view(request):
    return render(request, 'accounts/profile/view.html')

@login_required
def my_advisor(request):
    return render(request, 'accounts/profile/my-advisor.html')

# used for signing up advisors
def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #user.groups.add(Group.objects.get(name='Advisors'))
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('index') # not redirecting????
        else:
            form = UserCreationForm()
    return render(request, 'accounts/advisor/signup.html', {'form': form})

def invite_advisor(request):
    form = InviteAdvisorForm()
    if request.method == 'POST':
        form = InviteAdvisorForm(request.POST)
        if form.is_valid():
            # form.save()
            email = form.cleaned_data.get('advisor_email')
            if not Invitation.objects.filter(email=email):
                invite = Invitation.create(email, inviter=request.user)
                invite.send_invitation(request)
                messages.success(request, 'An email invitation has been sent to your advisor')
            else:
                messages.error(request, 'Advisor already invited')
            return redirect('index') # TODO: redirect to thank you page
    else:
        form = InviteAdvisorForm()
    return render(request, 'accounts/profile/my-advisor.html', {'form' : form})

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = StudentProfileForm(request.POST, instance=request.user.studentprofile)
        if profile_form.is_valid() and user_form.is_valid():
            # if blank, use last saved entry
            # if not user_form.data['email']:
            #     user_form.cleaned_data['email'] = User.objects.get(id=request.user.id).email
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile_view')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        profile_form = StudentProfileForm()
        user_form = UserForm()
    return render(request, 'accounts/profile/edit.html', {'prof_form' : profile_form, 'user_form' : user_form})
