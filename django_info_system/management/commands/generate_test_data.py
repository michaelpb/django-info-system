from django.core.management.base import BaseCommand, CommandError
import sys
import os.path
from django.apps import apps


from django.conf import settings


def create_user(username=None, first_name=None, last_name=None, is_super=False):
    User = apps.get_model(settings.AUTH_USER_MODEL.rsplit('.', 1))
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

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not settings.DEBUG:
            raise CommandError('Cannot run unless in DEBUG mode')
        create_user('janetest', is_super=True)
        create_user('joetest', is_super=True)
        create_user('alicetest')
        create_user('bobtest')
        create_user('charlietest')
        create_user('diditest')

