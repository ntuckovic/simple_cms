# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import LoginView, LogoutView, UpdateProfileView


urlpatterns = [
    url(r'^login/?$', LoginView.as_view(), name='login'),
    url(r'^logout/?$', LogoutView.as_view(), name='logout'),
    url(r'^profile/?$', UpdateProfileView.as_view(), name='profile'),
]
