from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from forms import CourseForm, ScheduleForm, AddTermForm
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
def schedules(request):
    return redirect('index')

@login_required
def new_schedule(request):
    if request.method == "POST":
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.owner = StudentProfile.objects.get(user_id=request.user.id)
            schedule.save()

            # Make dummy course session
            sesh = CourseSession(term=4747, semester='FA', schedule=schedule)
            sesh.save()

            # Add all previous courses
            for course in form.cleaned_data['classes_taken']:
                sesh.courses.add(course)
                sesh.save()

            # Save it to the schedule's course session
            schedule.course_sessions.add(sesh)
            schedule.save()

            remaining_courses = makeQueue(schedule.id)
            makeBlankSchedule(remaining_courses, schedule.id)
            messages.success(request, 'Your schedule was successfully made!')
            return redirect('my_schedules')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ScheduleForm()
    return render(request, 'schedules/new_schedule.html', {'form': form})

@login_required
def edit_schedule(request, schedule_id):
    sched = get_object_or_404(Schedule, pk=schedule_id)
    remaining_courses = sched.course_sessions.filter(term=4848)[0].courses.all()
    sessions = sched.course_sessions.all().order_by('term').exclude(term=4848).exclude(term=4747)

    if sched.owner.user != request.user:
        # TODO: edit private html to show different message if view/edit
        return render(request, 'schedules/private.html')

    courses = -1
    add_form = None
    if request.GET.get('search'):
        search = request.GET.get('search')
        courses = Course.objects.filter(course_name__icontains=search)

        add_form = AddTermForm(sessions=sessions)


    return render(request, 'schedules/edit_schedule.html',
        {'remaining_courses': remaining_courses,
        'sessions' : sessions,
        'courses' : courses,
        'add_form' : add_form
        })

# @login_required
# class CourseSearchListView(CourseListView):
    
#     def get_queryset(self):
#         result = super(CourseSearchListView, self).get_queryset()

#         query = self.request.GET.get('q')
#         if query:
            

# TODO: Test if removing login_required breaks request.user
@login_required
def detail(request, schedule_id):
    # Get the schedule 
    sched = get_object_or_404(Schedule, pk=schedule_id)

    # Check to see requester is the owner, if it's private
    if sched.owner.user != request.user and not sched.public:
        return render(request, 'schedules/private.html')

    return render(request, 'schedules/detail.html', {'title': sched.title, 'sessions' : sched.course_sessions.all().order_by('term')})

def private(request):
    return render(request, 'schedules/private.html')