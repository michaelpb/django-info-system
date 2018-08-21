from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils.translation import ugettext as _

from .forms import EditPersonForm

# 1st party
from django_info_system.generic_views import (
    ListInfo,
    ViewOverviewInfo,
    ViewActivityInfo,
    ManageEditInfo,
)

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
            'all': (lambda qs: qs),
            None: 'all', # default
        }

class PersonList(ListInfo, Base):
    breadcrumb = _('People')

class PersonView(ViewOverviewInfo, Base):
    parent_view = PersonList

class PersonManageEdit(ManageEditInfo, Base):
    parent_view = PersonView
    form = EditPersonForm

