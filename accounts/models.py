from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, AbstractUser

from dept_codes import DEPTS

class CustomUser(AbstractUser):
	types = (
		('S', 'Student'),
		('A', 'Advisor')
	)
	user_type = models.CharField(
		max_length=2,
		choices=types,
		default='S'
	)


class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name='user_profile')
	
	email = models.EmailField()
	avatar = models.ImageField(upload_to='uploads/', null=True)
	full_name = models.CharField(max_length=50, default='Cecil Sagehen')

	year = models.IntegerField(default=2020, null=True)
	
	dept = models.CharField(
		max_length=4,
		choices = DEPTS,
		default = 'CSCI'
	)

	def __unicode__(self):
		return '{} - {} - {}'.format(self.user.username, self.full_name, self.email)