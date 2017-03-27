from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Schedule(models.Model):
	owner = models.OneToOneField(User, related_name='user_schedule')

	start_sem = models.CharField(max_length=4) # [FA|SP][\d\d]
	end_sem = models.CharField(max_length=4)

	visibility = models.BooleanField(default=False)

class Courses(models.Model):
	course_id = models.CharField(max_length=9) # e.g. CHEM170A or '\w{2,4}\d+\w?'
	area =
	credit =
	link =

class Session(models.Model):
	term = models.IntegerField(default=2017)

	SEMS = (
		('FA' , 'Fall'),
		('SP' , 'Spring')
	)
	semester = models.CharField(
		max_length=2,
		choices = SEMS
	)

	days_meet = models.CharField(max_length=5) # how to deal with classes that meet multiple times a week but at different times per day (e.g. a course has two sessions?? Not include time meet?)

	class Meta:
		unique_together = (("term", "semester"),)