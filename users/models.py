# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from simple_cms.mixins.models import GenderMixin, NameMixin


@python_2_unicode_compatible
class UserProfile(GenderMixin, NameMixin, models.Model):
    user = models.OneToOneField(
        User, verbose_name=_('User'),
        related_name='profile',
        on_delete=models.CASCADE
    )
    avatar = models.ImageField(
        verbose_name=_('Avatar'), blank=True)
    can_comment = models.BooleanField(
        verbose_name=_('Can comment'), default=True)
    can_login = models.BooleanField(verbose_name=_('Can login'), default=True)
    date_of_birth = models.DateField(
        verbose_name=_('Date of birth'), blank=True, null=True)
    address_street = models.CharField(
        verbose_name=_('Street'), max_length=150, blank=True, default='')
    address_place = models.CharField(
        verbose_name=_('Place'), max_length=150, blank=True, default='')
    address_postcode = models.CharField(
        verbose_name=_('Postal code'), max_length=10, blank=True, default='')
    country = models.CharField(
        verbose_name=_('Country'), max_length=100, blank=True, default='')

    def __str__(self):
        return self.full_name
