from __future__ import unicode_literals

from django.db import models

class Schedule(models.Model):
    # Use django default id number as primary key
    owner = models.ForeignKey('accounts.Profile')
    start_sem = models.CharField(max_length=4) # FA\d{2}|SP\d{2}
    end_sem = models.CharField(max_length=4)

    # date of creation (and update?)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    public = models.BooleanField(default=False)

    def __unicode__(self):
        return "Schedule owner: {}".format(self.owner)

class Course(models.Model):
    course_id = models.CharField(max_length=9) # e.g. CHEM170A or '\w{2,4}\d+\w?'
    
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
        ('Full', '1.0'),
        ('Half', '0.5'),
        ('Qrtr', '0.25'),
    )
    credit = models.CharField(
        max_length=4,
        choices = credit_opts
    )

    link = models.URLField()

    def __unicode__(self):
        return "{}".format(self.course_id)

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