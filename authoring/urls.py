# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import LoginView, LogoutView, DashboardView, ArticlesListView, \
    ArticleUpdateView, ArticleCreateView


urlpatterns = [
    url(r'^login/?$', LoginView.as_view(), name='login'),
    url(r'^logout/?$', LogoutView.as_view(), name='logout'),
    url(r'^dashboard/?$', DashboardView.as_view(), name='dashboard'),
    url(r'^articles/(?P<page>[0-9]+)/$',
        ArticlesListView.as_view(), name='articles_list'),
    url(r'^articles/update/(?P<pk>[0-9]+)/$',
        ArticleUpdateView.as_view(), name='articles_update'),
    url(r'^articles/create/$',
        ArticleCreateView.as_view(), name='articles_create'),
]
