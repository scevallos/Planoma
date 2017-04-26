from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from forms import CourseForm, ScheduleForm #, ClassesTakenForm
from accounts.models import StudentProfile
from schedules.models import *
from make_schedule import *


@login_required
def add_course(request):
    form = CourseForm()
    return render(request, 'courses/course_new.html', {'form': form})

@login_required
def my_schedules(request):
    # Get the latest 3 schedules made by the user
    latest_scheds = Schedule.objects.all().filter(owner_id=request.user.id).order_by('-created_at')[:3]
    context = {'latest_scheds': latest_scheds}
    return render(request, 'schedules/my_schedules.html', context)
    # return render(request, 'schedules/my_schedules.html')

@login_required
def new_schedule(request):
    if request.method == "POST":
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.owner = StudentProfile.objects.get(user_id=request.user.id)
            schedule.save()
            remaining_courses = makeQueue(schedule.id)
            makeBlankSchedule(remaining_courses, schedule.id)
            return redirect('my_schedules')
    else:
        form = ScheduleForm()
    return render(request, 'schedules/new_schedule.html', {'form': form})

@login_required
def detail(request, schedule_id):
    # Get the schedule 
    sched = get_object_or_404(Schedule, pk=schedule_id)

    # Check to see requester is the owner, if it's private
    if sched.owner.user != request.user and not sched.public:
        return render(request, 'schedules/private.html')

    return render(request, 'schedules/detail.html', {'schedule': sched})

def private(request):
    return render(request, 'schedules/private.html')