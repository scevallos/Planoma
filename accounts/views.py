from django.shortcuts import render
from django.http import Http404

from accounts.models import UserProfile


def index(request):
	return render(request, 'accounts/index.html',)

def profile(request):
	return render(request, 'accounts/profile.html')