from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from forms import CourseForm, ScheduleForm
from accounts.models import StudentProfile
<<<<<<< HEAD
from schedules.models import *
=======
from make_schedule import makeQueue, makeSchedule
>>>>>>> 139a312beb5e79b28a39d1801aeccdabe873beb1

@login_required
def add_course(request):
    form = CourseForm()
    return render(request, 'courses/course_new.html', {'form': form})

@login_required
def my_schedules(request):
    # Get the latest 3 schedules made by the user
    # latest_scheds = Schedule.objects.all().filter(owner_id=request.user.id).order_by('-created_at')[:3]
    # context = {'latest_scheds': latest_scheds}
    # return render(request, 'schedules/my_schedules.html', context)
    return render(request, 'schedules/my_schedules.html')

@login_required
def new_schedule(request):
    if request.method == "POST":
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.owner = StudentProfile.objects.get(user_id=request.user.id)
            schedule.save()
            ## still need to make course sessions???? Not sure how those really work with this view
            remaining_courses = makeQueue(request.user.id, schedule.id)
            makeSchedule(schedule.start_sem, schedule.end_sem, remaining_courses, 4, schedule.id)
            return redirect('my_schedules')
    else:
        form = ScheduleForm()
    return render(request, 'schedules/new_schedule.html', {'form': form})