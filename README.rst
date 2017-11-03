=============================
Django Info System
=============================

.. image:: https://badge.fury.io/py/django-info-system.svg
    :target: https://badge.fury.io/py/django-info-system

.. image:: https://travis-ci.org/michaelpb/django-info-system.svg?branch=master
    :target: https://travis-ci.org/michaelpb/django-info-system

.. image:: https://codecov.io/gh/michaelpb/django-info-system/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/michaelpb/django-info-system

* **WIP NOTE:** This is a project spun off of internal
  apps developed for [Open Lab](http://openlab.org/)
  for use with other similarly structured. It's still
  in the process of becoming a well-documented and
  generally useful free/libre library, meaning it's API
  is not well documented and is subject to rapid
  change.

* **NOTE:** Presently *only* supports Python 3.5+ and Django 1.9+

System of generic views and abstract models to permit
objects with hierarchical tab view and editing



Quick start
------------

**Overview:**

1. Install django-info-system and put in requirements file
2. Add to INSTALLED_APPS
3. TODO finish this list :)

---------------

1. Install
~~~~~~~~~~

Install Django Info System::

    pip install django-info-system


2. Add to INSTALLED_APPS
~~~~~~~~~~~~~~~~~~~~~~~~

In your ``settings.py`` file, add something like:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_info_system.apps.DjangoInfoSystemConfig',
        ...
    )


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
