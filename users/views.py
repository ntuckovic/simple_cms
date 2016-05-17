# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from simple_cms.mixins.views import LoginViewMixin, LogoutViewMixin


class LoginView(LoginViewMixin):
    success_url = '/'


class LogoutView(LogoutViewMixin):
    url = '/'
