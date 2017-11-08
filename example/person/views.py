from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils.translation import ugettext as _

# 1st party
from django_info_system.generic_views import ListInfo

# local
from .models import Person

class Base:
    """
    Mix-in to establish everything about teams.

    When subclassing more core generic views, add this in to get all the magic.
    """
    model = Person
    noun = 'person'
    model_class = 'person'
    field = 'id'
    template_prefix = 'person/'
    actions = []
    extra_form = None
    member_field_names = []

    browse_tabs = {
            'active': (lambda qs: qs.filter(account__isnull=False)),
            'all': False,
            None: 'all', # default
        }

class PersonList(ListInfo, Base):
    breadcrumb = _('People')

