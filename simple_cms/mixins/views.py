# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.http import is_safe_url

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import REDIRECT_FIELD_NAME, \
    login as auth_login, logout as auth_logout

from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView


class LoginViewMixin(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super(LoginViewMixin, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())

        # If the test cookie worked, go ahead and
        # delete it since its no longer needed
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()

        return super(LoginViewMixin, self).form_valid(form)

    def get_success_url(self):
        redirect_to = self.request.POST.get(self.redirect_field_name)
        if not is_safe_url(url=redirect_to, host=self.request.get_host()):
            redirect_to = self.success_url

        return redirect_to


class LogoutViewMixin(RedirectView):
    def get(self, request, *args, **kwargs):
        auth_logout(request)

        return super(LogoutViewMixin, self).get(request, *args, **kwargs)


class MenuMixin(object):
    def get_context_data(self, **kwargs):
        context_data = super(MenuMixin, self).get_context_data(
            **kwargs
        )
        context_data['menu_items'] = self.get_menu_settings()

        return context_data

    def get_menu_settings(self):
        '''
        override this method and return menu dict
        '''

        return []


class ActiveItemMixin(object):
    active_menu_name = None

    def get_context_data(self, **kwargs):
        context_data = super(ActiveItemMixin, self).get_context_data(
            **kwargs
        )
        context_data['active_menu_name'] = self.active_menu_name

        return context_data
