from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'people/', include('person.urls')),
    url(r'admin/', admin.site.urls),
    # url(r'', include('django-info-system.urls', namespace='django-info-system')),
]
