from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from forms import CourseForm, ScheduleForm
from accounts.models import StudentProfile

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
            return redirect('mycals')
    else:
        form = ScheduleForm()
    return render(request, 'schedules/new_schedule.html', {'form': form})