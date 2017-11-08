from django.conf.urls import url

from django_info_system.generic_views import url_helper as u

from person import views

urlpatterns = [
    u(r'^$', views.PersonList),
    u(r'^(?P<tab>[a-z][a-z][a-z]+)$', views.PersonList,
        url_name_suffix="_tab"),
]
