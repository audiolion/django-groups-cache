from django.core.cache import cache
from .default_settings import CACHE_TIMEOUT


def generate_cache_key(user):
    return "groups:middleware:{0}".format(user.id)

def get_group(user):
    """ Rather than throw an error on get_group, we just return None.
        Makes handling of anonymous users in non-loggedin areas easier.
    """
    if user.is_anonymous():
        return None

    key = generate_cache_key(user)
    groups = cache.get(key)
    if groups is not None:
        return groups
    groups = user.groups.all()
    cache.set(key, groups, CACHE_TIMEOUT)
    return groups
