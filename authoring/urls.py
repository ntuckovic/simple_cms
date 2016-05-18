# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import LoginView, LogoutView, DashboardView, \
    ArticlesListView, ArticleUpdateView, ArticleCreateView, ArticleDeleteView, \
    TagsListView, TagsUpdateView, TagsCreateView, TagsDeleteView, \
    CategoryListView, CategoryUpdateView, CategoryCreateView, CategoryDeleteView


urlpatterns = [
    url(r'^login/?$', LoginView.as_view(), name='login'),
    url(r'^logout/?$', LogoutView.as_view(), name='logout'),
    url(r'^dashboard/?$', DashboardView.as_view(), name='dashboard'),
    # Articles
    url(r'^articles/(?P<page>[0-9]+)/$',
        ArticlesListView.as_view(), name='articles_list'),
    url(r'^articles/update/(?P<pk>[0-9]+)/$',
        ArticleUpdateView.as_view(), name='articles_update'),
    url(r'^articles/delete/(?P<pk>[0-9]+)/$',
        ArticleDeleteView.as_view(), name='articles_delete'),
    url(r'^articles/create/$',
        ArticleCreateView.as_view(), name='articles_create'),
    # Tags
    url(r'^tags/(?P<page>[0-9]+)/$',
        TagsListView.as_view(), name='tags_list'),
    url(r'^tags/update/(?P<pk>[0-9]+)/$',
        TagsUpdateView.as_view(), name='tags_update'),
    url(r'^tags/delete/(?P<pk>[0-9]+)/$',
        TagsDeleteView.as_view(), name='tags_delete'),
    url(r'^tags/create/$',
        TagsCreateView.as_view(), name='tags_create'),
    # Category
    url(r'^category/(?P<page>[0-9]+)/$',
        CategoryListView.as_view(), name='categories_list'),
    url(r'^category/update/(?P<pk>[0-9]+)/$',
        CategoryUpdateView.as_view(), name='categories_update'),
    url(r'^category/delete/(?P<pk>[0-9]+)/$',
        CategoryDeleteView.as_view(), name='categories_delete'),
    url(r'^category/create/$',
        CategoryCreateView.as_view(), name='categories_create'),
]
