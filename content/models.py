# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Category(models.Model):
    title = models.CharField(max_length=350)
    parent = models.ForeignKey(
        'self', verbose_name=_('Parent category'), null=True, blank=True,
        on_delete=models.PROTECT, related_name='subcategories')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


@python_2_unicode_compatible
class Tag(models.Model):
    title = models.CharField(max_length=350)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Article(models.Model):
    created_date = models.DateTimeField(
        verbose_name=_('Created on'), auto_now_add=True)
    last_change = models.DateTimeField(
        verbose_name=_('Last change'), auto_now=True)
    title = models.CharField(max_length=350)
    author = models.ForeignKey(
        User,
        verbose_name=_('Author'),
        related_name='author',
        on_delete=models.CASCADE
    )
    content = models.TextField(default='', blank=True)
    published = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True)
    tags = models.ManyToManyField(Tag, verbose_name=_('Tags'), blank=True)

    @property
    def has_been_modified(self):
        return self.created_date != self.last_change

    def __str__(self):
        return self.title
