# from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.template import loader
from django.contrib import messages
from django.db import transaction

from models import StudentProfile
from schedules.models import Schedule, Course, CourseSession
from forms import UserForm, StudentProfileForm


def index(request):
    return render(request, 'index.html',)

def contact_us(request):
    return render(request, 'contact-us.html',)

@login_required
def profile_view(request):
    return render(request, 'accounts/profile/view.html')

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = StudentProfileForm(request.POST, instance=request.user.studentprofile)
        if profile_form.is_valid() and user_form.is_valid():
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