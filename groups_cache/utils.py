from django.core.cache import cache
from .default_settings import CACHE_TIMEOUT

from hashids import Hashids


hashids = Hashids(min_length=5)

def generate_cache_key(user):
    hashid = hashids.encode(user.id)
    return "groups:middleware:{0}".format(hashid)

def cache_groups(user):
    # user must be authenticated to cache groups
    if not user.is_authenticated():
        return None

    key = generate_cache_key(user)
    groups = cache.get(key)
    if groups is not None:
        return groups
    groups = user.groups.all().values_list('name', flat=True)
    cache.set(key, groups, CACHE_TIMEOUT)
    return groups
