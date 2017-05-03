from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from dept_codes import DEPTS
from django.contrib.auth.models import Group

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
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
    YEAR_CHOICES = [(r,r) for r in xrange(2010, (datetime.now().year+5))]
    year = models.IntegerField(
        choices=YEAR_CHOICES,
        default=datetime.now().year
    )
    adv = models.ForeignKey('AdvisorProfile', null=True, on_delete=models.SET_NULL)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            StudentProfile.objects.create(user=instance)
            instance.groups.add(Group.objects.get(name='Students'))

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        try:
            instance.studentprofile.save()
        except:
            pass
