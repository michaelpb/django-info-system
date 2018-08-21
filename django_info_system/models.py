from django.db import models
from django.utils.translation import ugettext as _
from django.conf import settings
from django.core.urlresolvers import reverse

class UpdateMixin(object):
    def update_fields(self, **kwds):
        for key, val in list(kwds.items()):
            setattr(self, key, val)

class InfoBaseModel(models.Model, UpdateMixin):
    PLACEHOLDER_IMAGE_URL = settings.STATIC_URL + 'django_info_system/images/placeholder.png'

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

    def get_actable_relations(self, event):
        return {
            'subject': self.user,
            'object': self,
        }

    def get_actable_json(self, event):
        verb = 'created' if event.is_creation else 'updated'
        actor_url = (
            self.user.get_absolute_url()
            if hasattr(self.user, 'get_absolute_url')
            else ''
        )
        return {
            'actor': str(self.user),
            'actor_url': actor_url,
            'verb': verb,
            'target': str(self),
            'target_url': self.get_absolute_url(),
        }

    def get_absolute_url(self):
        name = self.__class__.__name__.lower()
        return reverse(name, args=[self.id])

    def editable_by(self, user):
        if not user.is_authenticated():
            return False

        if user == self.user:
            return True

        # Add permissions system later here
        return False

    def __str__(self):
        return self.name

    def get_thumb_url(self):
        return self.PLACEHOLDER_IMAGE_URL

