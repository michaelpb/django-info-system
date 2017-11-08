from django.db import models
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify
from django_info_system.models import InfoBaseModel
from django.conf import settings

class Person(InfoBaseModel):
    account = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='associated_person',
        help_text=_("Account associated with profile"),
        verbose_name=_("Account"),
        null=True,
        blank=True,
    )

    email = models.EmailField(null=True, blank=True)

