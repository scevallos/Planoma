from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from dept_codes import DEPTS

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
    @receiver(post_save, sender=User)
    def create_advisor_profile(sender, instance, created, **kwargs):
        if created:
            AdvisorProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.advisorprofile.save()


class StudentProfile(UserProfile):
    YEAR_CHOICES = []
    for r in range(2010, (datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))
    year = models.IntegerField(
        choices=YEAR_CHOICES,
        default=datetime.now().year
    )
    adv = models.ForeignKey('AdvisorProfile', null=True, on_delete=models.SET_NULL)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            StudentProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.studentprofile.save()

