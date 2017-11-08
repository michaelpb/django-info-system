from django.db import models
from django.utils.translation import ugettext as _
from django.conf import settings

class UpdateMixin(object):
    def update_fields(self, **kwds):
        for key, val in list(kwds.items()):
            setattr(self, key, val)

class InfoBaseModel(models.Model, UpdateMixin):
    # Example use of placeholder:
    # PLACEHOLDER_IMAGE_URL = settings.STATIC_URL + 'core/images/placeholder.png'

    class Meta:
        abstract = True
        get_latest_by = "updated_date"

    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            null=True,
                            blank=True,
                            verbose_name='Creator')
    name = models.CharField(blank=True, max_length=255)

    description = models.TextField(
            default="", blank=True,
            help_text=_("Notes or description"),
            verbose_name=_("Description"))

    def editable_by(self, user):
        if not user.is_authenticated():
            return False

        if user == self.user:
            return True

        return bool(self.members.filter(id=user.id))

    def __str__(self):
        return self.title

    def get_thumb_url(self):
        return self.PLACEHOLDER_IMAGE_URL

