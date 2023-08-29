# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
    urlpatterns += (path("debug/", include("debug_toolbar.urls")),)