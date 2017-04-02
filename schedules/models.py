from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
    course_id = models.CharField(max_length=9, primary_key=True) # e.g. CHEM170A or '\w{2,4}\d+\w?'
    
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
    link = models.URLField(null=True, blank=True)

    # defining pre-req relationship as foreign key to self
    pre_req = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return "{}".format(self.course_id)

class EquivCourses(models.Model):
    course_one = models.ForeignKey(Course, related_name='course_one')
    course_two = models.ForeignKey(Course, related_name='course_two')
    equiv_to = models.ForeignKey(Course, related_name='equiv_to')

class CourseSession(models.Model):
    course = models.ManyToManyField(Course)
    term = models.IntegerField(default=2017) # The year the course is taking place

    SEMS = (
        ('FA' , 'Fall'),
        ('SP' , 'Spring')
    )
    semester = models.CharField( # Either Spring or Fall to identify the semester
        max_length=2,
        choices = SEMS
    )

    # Not sure if we really need this
    # days_meet = models.CharField(max_length=5) # one or more of 'MTWRF'

    class Meta:
        unique_together = (('term', 'semester'),)
        ordering = ('term', 'semester', )

class Schedule(models.Model):
    # Use django default id number as primary key
    owner = models.ForeignKey('accounts.StudentProfile', on_delete=models.CASCADE)
    start_sem = models.CharField(max_length=4) # FA\d{2}|SP\d{2}
    end_sem = models.CharField(max_length=4)

    # date of creation and last update time
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    public = models.BooleanField(default=False)

    course_sessions = models.ManyToManyField(CourseSession)

    def __unicode__(self):
        return "Schedule owner: {}".format(self.owner)