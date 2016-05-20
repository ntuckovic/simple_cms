# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.urlresolvers import reverse

from django.views.generic import ListView, \
    TemplateView, CreateView, DeleteView
from django.views.generic.edit import UpdateView

from content.models import Article, Tag, Category
from simple_cms.mixins.views import LoginViewMixin, LogoutViewMixin,\
    MenuMixin, ActiveItemMixin


class LoginView(LoginViewMixin):
    success_url = '/authoring/dashboard/'


class LogoutView(LogoutViewMixin):
    url = '/authoring/login/'


class AuthoringUserPassesTestMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class AutoringLoginRequiredMixin(
        AuthoringUserPassesTestMixin,
        MenuMixin, ActiveItemMixin, LoginRequiredMixin):
    login_url = '/authoring/login/'

    def get_menu_settings(self):
        return getattr(settings, 'AUTHORING').get('MENU_ITEMS')


class DashboardView(AutoringLoginRequiredMixin, TemplateView):
    template_name = 'authoring/dashboard.html'


class ArticlesListView(AutoringLoginRequiredMixin, ListView):
    template_name = 'authoring/articles_list.html'
    model = Article
    paginate_by = 20
    active_menu_name = 'Articles'


class ArticleDetailMixin(AutoringLoginRequiredMixin):
    fields = ['title', 'content', 'published', 'category', 'tags']
    model = Article
    active_menu_name = 'Articles'

    def get_success_url(self):
        return reverse('authoring:articles_list', args=[1])


class ArticleUpdateView(ArticleDetailMixin, UpdateView):
    template_name = 'authoring/article_detail.html'


class ArticleCreateView(ArticleDetailMixin, CreateView):
    template_name = 'authoring/article_detail_new.html'

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        return super(ArticleCreateView, self).form_valid(form)


class ArticleDeleteView(AutoringLoginRequiredMixin, DeleteView):
    template_name = 'authoring/article_confirm_delete.html'
    success_url = '/authoring/articles/1/'
    model = Article
    active_menu_name = 'Articles'


class TagsListView(AutoringLoginRequiredMixin, ListView):
    template_name = 'authoring/tags_list.html'
    model = Tag
    paginate_by = 20
    active_menu_name = 'Tags'


class TagsDetailMixin(AutoringLoginRequiredMixin):
    fields = ['title', 'is_active']
    model = Tag
    active_menu_name = 'Tags'

    def get_success_url(self):
        return reverse('authoring:tags_list', args=[1])


class TagsUpdateView(TagsDetailMixin, UpdateView):
    template_name = 'authoring/tags_detail.html'


class TagsCreateView(TagsDetailMixin, CreateView):
    template_name = 'authoring/tags_detail_new.html'


class TagsDeleteView(AutoringLoginRequiredMixin, DeleteView):
    template_name = 'authoring/tags_confirm_delete.html'
    success_url = '/authoring/tags/1/'
    model = Tag
    active_menu_name = 'Tags'


class CategoryListView(AutoringLoginRequiredMixin, ListView):
    template_name = 'authoring/category_list.html'
    model = Category
    paginate_by = 20
    active_menu_name = 'Categories'


class CategoryDetailMixin(AutoringLoginRequiredMixin):
    fields = ['title', 'parent']
    model = Category
    active_menu_name = 'Categories'

    def get_success_url(self):
        return reverse('authoring:categories_list', args=[1])


class CategoryUpdateView(CategoryDetailMixin, UpdateView):
    template_name = 'authoring/category_detail.html'


class CategoryCreateView(CategoryDetailMixin, CreateView):
    template_name = 'authoring/category_detail_new.html'


class CategoryDeleteView(AutoringLoginRequiredMixin, DeleteView):
    template_name = 'authoring/category_confirm_delete.html'
    success_url = '/authoring/category/1/'
    model = Category
    active_menu_name = 'Categories'
