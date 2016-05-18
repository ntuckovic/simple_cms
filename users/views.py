# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView

from simple_cms.mixins.views import LoginViewMixin, LogoutViewMixin

from .models import UserProfile


class LoginView(LoginViewMixin):
    success_url = '/'


class LogoutView(LogoutViewMixin):
    url = '/'


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'users/profile_update.html'
    success_url = '/users/profile/'
    model = UserProfile
    fields = [
        'first_name', 'last_name', 'gender',
        'avatar', 'date_of_birth', 'address_street',
        'address_place', 'address_postcode',
        'country', 'favorite_categories'
    ]

    def get_object(self, queryset=None):
        user = self.request.user

        return self.model.objects.get(user=user)
