from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'people/', include('person.urls')),
    # url(r'', include('django-info-system.urls', namespace='django-info-system')),
]
