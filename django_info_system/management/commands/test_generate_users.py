from django.core.management.base import BaseCommand, CommandError
import sys
import os.path

from django.conf import settings

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not settings.DEBUG:
            raise CommandError('Cannot run unless in DEBUG mode')

