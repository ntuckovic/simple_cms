# -*- coding: utf-8 -*-

from django.utils.http import is_safe_url

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import REDIRECT_FIELD_NAME, \
    login as auth_login, logout as auth_logout
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

from django.views.generic import FormView, RedirectView, ListView, \
    TemplateView, CreateView
from django.views.generic.edit import UpdateView

from content.models import Article


class LoginView(FormView):
    template_name = 'authoring/login.html'
    success_url = '/authoring/dashboard/'
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())

        # If the test cookie worked, go ahead and
        # delete it since its no longer needed
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()

        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        redirect_to = self.request.POST.get(self.redirect_field_name)
        if not is_safe_url(url=redirect_to, host=self.request.get_host()):
            redirect_to = self.success_url

        return redirect_to


class LogoutView(RedirectView):
    url = '/authoring/login/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)

        return super(LogoutView, self).get(request, *args, **kwargs)


class AutoringLoginRequiredMixin(LoginRequiredMixin):
    login_url = '/authoring/login/'


class DashboardView(AutoringLoginRequiredMixin, TemplateView):
    template_name = 'authoring/dashboard.html'


class ArticlesListView(ListView):
    template_name = 'authoring/articles_list.html'
    model = Article
    paginate_by = 20


class AuthorDetailMixin(object):
    fields = ['title', 'content', 'published', 'category', 'tags']
    model = Article

    def get_success_url(self):
        return reverse('authoring:articles_list', args=[1])


class ArticleUpdateView(AuthorDetailMixin, UpdateView):
    template_name = 'authoring/article_detail.html'


class ArticleCreateView(AuthorDetailMixin, CreateView):
    template_name = 'authoring/article_detail_new.html'

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        return super(ArticleCreateView, self).form_valid(form)
