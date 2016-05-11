# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin

from models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'can_comment', 'can_login', 'country']
    raw_id_fields = ['user']
    search_fields = ['user__username', 'first_name', 'last_name']
