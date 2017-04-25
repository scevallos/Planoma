from __future__ import unicode_literals

from django.db import models
from constants import *
from itertools import chain

class Course(models.Model):
    course_id = models.CharField(max_length=9, primary_key=True) # e.g. CHEM170A or '\w{2,4}\d+\w?'
    
    course_name = models.CharField(max_length=50)

    area_opts = (
        ('1', 'Area 1'),
        ('2', 'Area 2'),
        ('3', 'Area 3'),
        ('4', 'Area 4'),
        ('5', 'Area 5'),
        ('6', 'Area 6'),
    )
    area = models.CharField(
        max_length=1,
        choices = area_opts,
        null=True # there are like 2 GEOL courses that satisfy no area lol
    )

    overlay_opts = (
        ('W' , 'Writing Intensive'),
        ('WA', 'Writing Intesive/Analyzing Difference'),
        ('S' , 'Speaking Intensive'),
        ('SA' , 'Speaking Intensive/Analyzing Difference'),
        ('A' , 'Analyzing Difference'),
    )
    overlay = models.CharField(
        max_length = 2,
        choices = overlay_opts,
        null=True
    )

    credit_opts = (
        ('Full', '1.00'),
        ('Half', '0.50'),
        ('Qrtr', '0.25'),
        ('Zero', '0.00'), # for labs
    )
    credit = models.CharField(
        max_length=4,
        choices = credit_opts
    )

    # link to aspc page, if applicable
    # NOTE: don't really wanna do this anymore lol
    # link = models.URLField(null=True, blank=True)

    # defining pre-req relationship as foreign key to self
    # Making this its own model so it has its own table
    # pre_req = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return "{}".format(self.course_id)

class PrereqCourses(models.Model):
    course_req = models.ForeignKey(Course, related_name='course_req')
    course_take = models.ForeignKey(Course, related_name='course_take')

    def __unicode__(self):
        return "{} for {}".format(self.course_req, self.course_take)

    class Meta:
        unique_together = (('course_req', 'course_take'), )


class EquivCourses(models.Model):
    course_one = models.ForeignKey(Course, related_name='course_one')
    course_two = models.ForeignKey(Course, related_name='course_two')
    equiv_to = models.ForeignKey(Course, related_name='equiv_to')

    def __unicode__(self):
        return "{} == {} for {}".format(self.course_one, self.course_two, self.equiv_to)

    class Meta:
        unique_together = (('course_one', 'course_two', 'equiv_to'),)

class CourseSession(models.Model):
    schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE, related_name='schedule')
    courses = models.ManyToManyField(Course)
    term = models.IntegerField(default=2017) # The year the course is taking place

    SEMS = (
        ('FA' , 'Fall'),
        ('SP' , 'Spring')
    )
    semester = models.CharField( # Either Spring or Fall to identify the semester
        max_length=2,
        choices = SEMS
    )

    def __unicode__(self):
        return "{} {}".format(self.semester, self.term)

    class Meta:
        unique_together = (('schedule', 'term', 'semester'),)
        ordering = ('term', 'semester', )

class Schedule(models.Model):
    # Use django default id number as primary key
    owner = models.ForeignKey('accounts.StudentProfile', on_delete=models.CASCADE)
    start_sem = models.CharField(max_length=4, choices=TERM_CHOICES) # FA\d{2}|SP\d{2}
    end_sem = models.CharField(max_length=4, choices=TERM_CHOICES)

    # date of creation and last update time
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    public = models.BooleanField(default=False)

    # title for the schedule
    title = models.CharField(max_length=50, default='Untitled', blank=True)

    course_sessions = models.ManyToManyField(CourseSession, related_name='sessions')

    # Stuff needed for auto-gen
    existing_credits = models.CharField(choices = CREDIT_CHOICES, max_length=12, null=True, default=0)
    languages_completed = models.CharField(choices = LANGUAGE_CHOICES, max_length=12, null=True, default=0)
    math_completed = models.CharField(choices = MATH_CHOICES, max_length=12, null=True, default=None)


    def get_all_courses(self):
        return list(chain(*[session.courses.all() for session in self.course_sessions.all()]))


    def __unicode__(self):
        return "Schedule owner: {}".format(self.owner)