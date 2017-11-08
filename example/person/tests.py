from django.test import TestCase

from person.models import Person
from person.models import Person

from django_info_system.factories import get_random_word as rando
from django_info_system.factories import get_random_name
from django_info_system.factories import get_random_sentence

def create_person(user):
    # Create a person that is under this user
    Person.objects.create(
        user=user,
        email='%s@%s.com' % (rando(), rando()),
        name=get_random_name(),
        description=get_random_sentence(),
    )


def create_plist(user):
    plist = Plist.objects.create(
        user=user,
        name=get_random_word() + ' list',
        description=get_random_sentence(),
    )

    persons = list(Person.objects.all())
    for x in range(plist.id):
        if x < len(persons):
            plist.people.add(persons[x])

