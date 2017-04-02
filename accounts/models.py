from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from annoying.fields import AutoOneToOneField


from datetime import datetime
from dept_codes import DEPTS

class UserProfile(models.Model):
    user = AutoOneToOneField(User, primary_key=True)
    dept = models.CharField(
        max_length=4,
        choices = DEPTS,
        default = 'CSCI'
    )

    def __unicode__(self):
        return '{} - {}'.format(self.user, self.dept)

    class Meta(object):
        abstract = True

class AdvisorProfile(UserProfile):
    pass


class StudentProfile(UserProfile):
    YEAR_CHOICES = []
    for r in range(2010, (datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))
    year = models.IntegerField(
        choices=YEAR_CHOICES,
        default=datetime.now().year
    ) # default to being a first-year lol
    adv = models.ForeignKey('AdvisorProfile', null=True, on_delete=models.SET_NULL)

