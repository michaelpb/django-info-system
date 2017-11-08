from django.core.management.base import BaseCommand, CommandError
import sys
import os.path
from django.apps import apps
import importlib

import random

from django.conf import settings


def create_user(username=None, first_name=None, last_name=None, is_super=False):
    User = apps.get_model(*settings.AUTH_USER_MODEL.rsplit('.', 1))
    last_name = last_name or 'Test'
    first_name = username.replace('test', '').capitalize()

    email = '%s@test.com' % username
    password = 'asdf'
    if not User.objects.filter(username=username):
        user = User.objects.create_user(username, email, 'asdf')
    else:
        user = User.objects.get(username=username)
    user.is_superuser = is_super
    user.is_staff = is_super
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    print('creating user', user.username)
    return user

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not settings.DEBUG:
            raise CommandError('Cannot run unless in DEBUG mode')
        users = []
        users.append(create_user('janetest', is_super=True))
        users.append(create_user('joetest', is_super=True))

        for name in ['alicetest', 'bobtest', 'charlietest', 'diditest']:
            users.append(create_user(name))

        fac_strings = getattr(settings, 'INFO_SYSTEM_TEST_FACTORIES', [])
        for fac_string in fac_strings:
            mod_name, func_name = fac_string.rsplit('.', 1)
            fac_module = importlib.import_module(mod_name)
            fac_method = getattr(fac_module, func_name)
            for user in users:
                for i in range(random.randint(1, 10)):
                    fac_method(user)

