# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

from content.views import FrontpageView


urlpatterns = [
    url(r'^$', FrontpageView.as_view(), name='frontpage'),
    url(r'^content/', include('content.urls', namespace='content')),
    url(r'^authoring/', include('authoring.urls', namespace='authoring')),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^admin/', admin.site.urls)
]

if settings.DEBUG is True:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
