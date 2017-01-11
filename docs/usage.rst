=====
Usage
=====

To use django-groups-cache in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'groups_cache.apps.GroupsCacheConfig',
        ...
    )

Add django-groups-cache's URL patterns:

.. code-block:: python

    from groups_cache import urls as groups_cache_urls


    urlpatterns = [
        ...
        url(r'^', include(groups_cache_urls)),
        ...
    ]
