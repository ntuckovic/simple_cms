# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from model_utils import Choices


class GenderMixin(models.Model):
    GENDERS = Choices(
        ('M', 'Male'),
        ('F', 'Female'),
    )

    class Meta:
        abstract = True

    gender = models.CharField(max_length=1, choices=GENDERS)


class NameMixin(models.Model):
    first_name = models.CharField(max_length=350)
    last_name = models.CharField(max_length=350)

    class Meta:
        abstract = True

    @property
    def full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)
