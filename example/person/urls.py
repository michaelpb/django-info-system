from django.conf.urls import url

from django_info_system.generic_views import url_helper as u

from person import views

PERSON_REGEXP = r'^(?P<id>[0-9]+)/'

urlpatterns = [
    u(r'^$', views.PersonList),
    u(r'^(?P<tab>[a-z][a-z][a-z]+)$', views.PersonList,
        url_name_suffix="_tab"),

    u(PERSON_REGEXP + '$', views.PersonView),
    u(PERSON_REGEXP + '/edit/$', views.PersonManageEdit),
]
