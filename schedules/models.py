from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Schedule(models.Model):
    # Use django default id number as primary key
    owner = models.ForeignKey('accounts.Student')
    start_sem = models.CharField(max_length=4) # FA\d{2}|SP\d{2}
    end_sem = models.CharField(max_length=4)

    visibility = models.BooleanField(default=False)

    def __unicode__(self):
        return "Schedule owner: {}".format(self.owner)

class Course(models.Model):
    course_id = models.CharField(max_length=9) # e.g. CHEM170A or '\w{2,4}\d+\w?'
    area = # 1.0 or 0.5 or 0.25
    credit =
    link =

class CourseSession(models.Model):
    course = models.ForeignKey(Courses)
    term = models.IntegerField(default=2017) # The year the course is taking place in

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
        unique_together = (("term", "semester"),)