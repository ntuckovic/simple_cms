# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    url(r'^authoring/', include('authoring.urls', namespace='authoring')),
    url(r'^admin/', admin.site.urls)
]

if settings.DEBUG is True:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
