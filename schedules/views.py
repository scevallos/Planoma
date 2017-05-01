from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from forms import CourseForm, ScheduleForm, AddTermForm, firstYearForm, TermForm
from accounts.models import StudentProfile
from schedules.models import *
from make_schedule import *
from django.contrib.auth.models import Group
from group_decorator import *


# required permissions
@group_required('Advisors')
@login_required
def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        term_form = TermForm(request.POST)
        if form.is_valid() and term_form.is_valid():
            course = form.save()
            term = term_form.save(commit=False)
            term.schedule = Schedule.objects.get(pk=7)
            term_selected = term.term
            semester_selected = term.semester
            for sched in Schedule.objects.all():
                done = False
                # courses = sched.get_all_courses()
                try:
                    sesh = sched.course_sessions.get(term=term_selected, semester=semester_selected)
                    for cur_course in sesh.courses.all():
                        if cur_course.course_id.startswith("ELEC"):
                            sesh.courses.remove(cur_course)
                            sesh.courses.add(course)
                            sesh.save()
                            done = True
                        if done:
                            break
                except:
                    pass
                # for sesh in sched.course_sessions.all():
                #     if done:
                #         break


            messages.success(request, 'Course has been successfully added.')
        else:
            messages.error(request, 'Course adding failed, course not added.')
    else:
        form = CourseForm()
        term_form = TermForm()
    return render(request, 'courses/course_new.html', {'form': form, 'term_form' : term_form} )


@login_required
def my_schedules(request):
    if request.user.groups.all()[0] == Group.objects.get(name='Advisors'):
        return redirect('index')
    # Get the latest 3 schedules made by the user
    latest_scheds = Schedule.objects.all().filter(owner_id=request.user.id).order_by('-created_at')[:3]
    context = {'latest_scheds': latest_scheds}
    return render(request, 'schedules/my_schedules.html', context)
    # return render(request, 'schedules/my_schedules.html')

@group_required('Students')
@login_required
def schedules(request):
    return redirect('index')
# TODO test if user not logged in, does it redirect back to original page

def new_schedule(request):
    return render(request, 'schedules/new_schedule.html')


@group_required('Students')
@login_required
def other_year(request):
    if request.method == "POST":
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.owner = StudentProfile.objects.get(user_id=request.user.id)

            schedule.save()

            # Make dummy course session
            sesh = CourseSession.objects.create(term=4747, semester='FA', schedule=)
            sesh.save()

            # Add all previous courses
            for course in form.cleaned_data['classes_taken']:
                sesh.courses.add(course)
                sesh.save()

            # Save it to the schedule's course session
            schedule.course_sessions.add(sesh)
            schedule.save()

            remaining_courses = makeQueue(schedule.id)
            status_code = makeBlankSchedule(remaining_courses, schedule.id) # we have a schedule with all the course sessions needed from 4848

            if status_code == -1:
                messages.error(request, 'Please select valid start and end semesters.')
            messages.success(request, 'Your schedule was successfully made!')
            return redirect('my_schedules')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ScheduleForm()
    return render(request, 'schedules/other_year.html', {'form': form})

@group_required('Students')
@login_required
def edit_schedule(request, schedule_id):
    sched = get_object_or_404(Schedule, pk=schedule_id)
    remaining_courses = sched.remaining_courses.courses.all()
    sessions = sched.course_sessions.all().order_by('term')

    if sched.owner.user != request.user:
        # TODO: edit private html to show different message if view/edit
        return render(request, 'schedules/private.html')

    courses = -1
    add_form = None
    # Search bar 
    if request.GET.get('search'):
        search = request.GET.get('search')
        courses = Course.objects.filter(course_name__icontains=search)

        add_form = AddTermForm(sessions=sessions, courses=courses)

        # User just hit save button from course searches
    if request.method == "POST":
        add_form = AddTermForm(request.POST, sessions=sessions, courses=courses)
        if add_form.is_valid():
            session = add_form.cleaned_data['terms']
            courses = add_form.courses

            # # Logic of is the course able to be taken -- pre-req stuff - TODO:
            # for course in courses:
            #     course
            #     PrereqCourses.objects.get(course_take=course)
            session.courses.add(courses[0])
            session.save()
            remaining_courses.remove(courses)
            remaining_courses.save()


        else:
            messages.error('Please select a valid semester.')



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


@group_required('Students')
@login_required
def first_year(request):
    if request.method == "POST":
        firstForm = firstYearForm(request.POST)
        if firstForm.is_valid():
            schedule = firstForm.save(commit=False)
            schedule.owner = StudentProfile.objects.get(user_id=request.user.id)
            schedule.save()
            # schedule.existing_credits=schedule.cleaned_data('existing_credits')

            status_code = makeSchedule(schedule.id)
            if status_code == -1:
                messages.error(request, 'Please select valid start and end semesters.')
            messages.success(request, 'Your schedule was successfully made!')
            return redirect('my_schedules')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        firstForm = firstYearForm()


    return render(request, 'schedules/first_year.html', {'firstForm': firstForm})

# @group_required('Students')
# @login_required
# def other_year(request):
#
#     return render(request, 'schedules/other_year.html')
#
# # TODO: Test if removing login_required breaks request.user

# @group_required('Students')
# @login_required
def detail(request, schedule_id):
    # Get the schedule
    sched = get_object_or_404(Schedule, pk=schedule_id)

    # Check to see requester is the owner, if it's private
    if sched.owner.user != request.user and not sched.public:
        return render(request, 'schedules/private.html')

    return render(request, 'schedules/detail.html', {'title': sched.title, 'sessions' : sched.course_sessions.all().order_by('term')})

def private(request):
    return render(request, 'schedules/private.html')
