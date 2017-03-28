from django.db import transaction
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404


def index(request):
	return render(request, 'accounts/index.html',)

@login_required
def profile(request):
	return render(request, 'accounts/profile.html')

@login_required
def mycals(request):
	return render(request, 'accounts/mycals.html')

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
