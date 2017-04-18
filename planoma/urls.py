"""planoma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from accounts import views as acc_views
from schedules import views as sch_views

urlpatterns = [
    url(r'^$', acc_views.index, name='index'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^accounts/mycals', acc_views.mycals, name='mycals'),
    url(r'^accounts/profile/view/', acc_views.profile_view, name='profile_view'),
    url(r'^accounts/profile/edit/', acc_views.update_profile, name='update_profile'),
    url(r'^schedules/new_schedule/', sch_views.new_schedule, name='new_schedule'),
    url(r'^courses/course_new/', sch_views.add_course, name='course_new'),
    url(r'^admin/', admin.site.urls),
]
