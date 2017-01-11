from django.conf import settings


CACHE_TIMEOUT = getattr(
    settings,
    'GROUPS_CACHE_TIMEOUT',
    500
)
