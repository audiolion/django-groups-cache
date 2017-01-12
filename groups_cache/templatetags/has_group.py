from django import template
from django.contrib.auth.models import Group
from django.core.cache import cache

from ..utils import generate_cache_key


register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    if not user.is_authenticated():
        return False
    key = generate_cache_key(user)
    groups = cache.get(key)
    if groups and group in groups:
        return True
    return False
