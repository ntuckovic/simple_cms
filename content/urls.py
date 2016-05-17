# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import ArticleView


urlpatterns = [
    url(r'^article/(?P<pk>[0-9]+)/$',
        ArticleView.as_view(), name='article'),
]
