# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^authoring/', include('authoring.urls', namespace='authoring')),
    url(r'^admin/', admin.site.urls),
]