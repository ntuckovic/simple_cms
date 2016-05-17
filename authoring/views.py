# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.urlresolvers import reverse

from django.views.generic import ListView, \
    TemplateView, CreateView
from django.views.generic.edit import UpdateView

from content.models import Article, Tag, Category
from simple_cms.mixins.views import LoginViewMixin, LogoutViewMixin


class LoginView(LoginViewMixin):
    success_url = '/authoring/dashboard/'


class LogoutView(LogoutViewMixin):
    url = '/authoring/login/'


class AuthoringUserPassesTestMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class AutoringLoginRequiredMixin(
        AuthoringUserPassesTestMixin, LoginRequiredMixin):
    login_url = '/authoring/login/'


class DashboardView(AutoringLoginRequiredMixin, TemplateView):
    template_name = 'authoring/dashboard.html'


class ArticlesListView(AutoringLoginRequiredMixin, ListView):
    template_name = 'authoring/articles_list.html'
    model = Article
    paginate_by = 20


class AuthorDetailMixin(AutoringLoginRequiredMixin):
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


class TagsListView(AutoringLoginRequiredMixin, ListView):
    template_name = 'authoring/tags_list.html'
    model = Tag
    paginate_by = 20


class TagsDetailMixin(AutoringLoginRequiredMixin):
    fields = ['title', 'is_active']
    model = Tag

    def get_success_url(self):
        return reverse('authoring:tags_list', args=[1])


class TagsUpdateView(TagsDetailMixin, UpdateView):
    template_name = 'authoring/tags_detail.html'


class TagsCreateView(TagsDetailMixin, CreateView):
    template_name = 'authoring/tags_detail_new.html'


class CategoryListView(AutoringLoginRequiredMixin, ListView):
    template_name = 'authoring/category_list.html'
    model = Category
    paginate_by = 20


class CategoryDetailMixin(AutoringLoginRequiredMixin):
    fields = ['title', 'parent']
    model = Category

    def get_success_url(self):
        return reverse('authoring:categories_list', args=[1])


class CategoryUpdateView(CategoryDetailMixin, UpdateView):
    template_name = 'authoring/category_detail.html'


class CategoryCreateView(CategoryDetailMixin, CreateView):
    template_name = 'authoring/category_detail_new.html'
