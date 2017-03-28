from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from dept_codes import DEPTS

class BaseUser(AbstractBaseUser):
    email = models.EmailField(primary_key=True)
    full_name = models.CharField(max_length=50, default='Cecil Sagehen')

    dept = models.CharField(
        max_length=4,
        choices = DEPTS,
        default = 'CSCI'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = USERNAME_FIELD

    def __unicode__(self):
        return '{} - {}'.format(self.full_name, self.email)

    class Meta:
        abstract = True

class GenericUser(BaseUser):
    pass

class Student(BaseUser):
    year = models.IntegerField(default=2020, null=True)
    avatar = models.ImageField(upload_to='uploads/', null=True)
    advisor = models.ForeignKey('Advisor', null=True, on_delete=models.SET_NULL)


class Advisor(BaseUser):
    pass
    

    