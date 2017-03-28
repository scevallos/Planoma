from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


from dept_codes import DEPTS

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dept = models.CharField(
        max_length=4,
        choices = DEPTS,
        default = 'CSCI'
    )

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    major = models.CharField(
        max_length=4,
        choices = DEPTS,
        default = 'CSCI'
    )
    year = models.IntegerField(
        max_length = 4,
        default= 1925
        )

class AdvisorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dept = models.CharField(
        max_length=4,
        choices = DEPTS,
        default = 'CSCI'
    )

    def __unicode__(self):
        return '{} - {}'.format(self.full_name, self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()