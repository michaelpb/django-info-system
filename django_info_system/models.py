from django.db import models
from django.utils.translation import ugettext as _
from django.conf import settings

# 1st party
from openlab.discussion.models import Thread

class UpdateMixin(object):
    def update_fields(self, **kwds):
        for key, val in list(kwds.items()):
            setattr(self, key, val)

class InfoBaseModel(UpdateMixin):
    # Example use of placeholder:
    # PLACEHOLDER_IMAGE_URL = settings.STATIC_URL + 'core/images/placeholder.png'

    class Meta:
        abstract = True
        get_latest_by = "updated_date"

    title = models.CharField(
            verbose_name=_("Name"),
            max_length=255)

    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    # tags = TaggableManager(
    #        help_text=_("Tags for the project"))

    summary = models.CharField(
            max_length=140,
            verbose_name=_("Summary"),
            help_text=_("Describe in in 140 characters or less. (No paragraphs.)"))

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

