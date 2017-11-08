from django.db import models

from person.models import Person

from django_info_system.models import InfoBaseModel

_ = str

class Plist(InfoBaseModel):
    people = models.ManyToManyField(
        'person.Person',
        related_name='lists',
        help_text='People in this list',
    )
    email = models.EmailField(null=True, blank=True)

