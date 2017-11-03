# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from django_info_system.urls import urlpatterns as django_info_system_urls

urlpatterns = [
    url(r'^', include(django_info_system_urls, namespace='django_info_system')),
]
