# from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.template import loader
from django.contrib import messages

from models import StudentProfile
from schedules.models import Schedule, Course, CourseSession
from forms import UserForm, StudentProfileForm


def index(request):
    return render(request, 'index.html',)

@login_required
def profile_view(request):
    return render(request, 'accounts/profile/view.html')

@login_required
def update_profile(request):
    # if request.method == 'POST':
    #     userForm = UserForm(request.POST, instance=request.user)
    #     profileForm = StudentProfileForm(request.POST, instance=request.user.profile)
    #     if form.is_valid():
    #         userForm.save()
    #         profileForm.save()
    #         messages.success(request, 'Your profile was successfully updated!')
    #         return redirect('settings:profile')
    #     else:
    #         messages.error(request, 'Please correct the error below.')
    # else:
    #     userForm = UserForm(instance=request.user)
    #     profileForm = StudentProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        userForm = UserForm(request.POST, instance=request.user)
        profileForm = StudentProfileForm(request.POST, instance=StudentProfile.objects.get(user_id=request.user.id))
        if profileForm.is_valid() and userForm.is_valid():
            userForm.save()
            profileForm.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile_view')
    else:
        profileForm = StudentProfileForm()
    return render(request, 'accounts/profile/edit.html')
    # if request.method == 'POST':
    #     user_form = UserForm(request.POST, instance=request.user)
    #     profile_form = ProfileForm(request.POST, instance=request.user.profile)
    #     if user_form.is_valid() and profile_form.is_valid():
    #         user_form.save()
    #         profile_form.save()
    #         messages.success(request, _('Your profile was successfully updated!'))
    #         return redirect('settings:profile')
    #     else:
    #         messages.error(request, _('Please correct the error below.'))
    # else:
    #     user_form = UserForm(instance=request.user)
    #     profile_form = ProfileForm(instance=request.user.profile)
    # return render(request, 'profiles/profile.html', {
    #     'user_form': user_form,
    #     'profile_form': profile_form
    # })

# def register(request):
#     if request.method == 'POST':
#         StudentProfileForm(request.user, request.POST)