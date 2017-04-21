from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from forms import CourseForm, ScheduleForm
from accounts.models import StudentProfile
from make_schedule import makeQueue, makeSchedule

@login_required
def add_course(request):
    form = CourseForm()
    return render(request, 'courses/course_new.html', {'form': form})

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
            return redirect('mycals')
    else:
        form = ScheduleForm()
    return render(request, 'schedules/new_schedule.html', {'form': form})