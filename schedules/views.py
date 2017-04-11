from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from forms import CourseForm, ScheduleForm

@login_required
def add_course(request):
    form = CourseForm()
    return render(request, 'courses/course_new', {'form': form})

@login_required
def new_schedule(request):
    form = ScheduleForm()
    return render(request, 'schedules/new_schedule', {'form': form})