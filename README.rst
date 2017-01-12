=============================
django-groups-cache
=============================

.. image:: https://badge.fury.io/py/django-groups-cache.png
    :target: https://badge.fury.io/py/django-groups-cache

.. image:: https://travis-ci.org/audiolion/django-groups-cache.png?branch=master
    :target: https://travis-ci.org/audiolion/django-groups-cache

Caches the groups a user is in so requests don't have to make calls to the database to check group status.

Documentation
-------------

The full documentation is at https://django-groups-cache.readthedocs.io.

Quickstart
----------

Install django-groups-cache::

    pip install django-groups-cache

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'groups_cache.apps.GroupsCacheConfig',
        ...
    )

Add the middleware to your `MIDDLEWARE_CLASSES`:

.. code-block:: python

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        ...
        'groups_cache.middleware.GroupsCacheMiddleware',
    )

Features
--------

* Adds `groups_cache` property to `request` object
* Provides templatetag `has_group`
* Invalidates cache on `User` or `Group` model changes

Checking in a Django Template if the user is in a group name:

.. code-block:: python

    {% if "admins" in request.groups_cache %}
      <a href="/admin">Admin Panel</a>
    {% endif %}

    # or use templatetag, note that templatetag is slower

    {% load has_group %}

    {% if request.user|has_group:"admins" %}
      <a href="/admin">Admin Panel</a>
    {% endif %}


Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
