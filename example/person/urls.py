from django.conf.urls import url

from django_info_system.generic_views import url_helper as u

from person import views

urlpatterns = [
    u(r'^$', views.PersonList),
]
