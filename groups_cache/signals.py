from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth.models import Group
from django.core.cache import cache
from django.dispatch import receiver

from .utils import generate_cache_key


@receiver(post_save, sender=settings.AUTH_USER_MODEL, dispatch_uid="invalidate_user")
def invalidate_user_cache(sender, **kwargs):
    key = generate_cache_key(kwargs.get('instance'))
    cache.delete(key)

@receiver(post_save, sender=Group, dispatch_uid="invalidate_group")
def invalidate_group_cache(sender, **kwargs):
    users = kwargs.get('instance').user_set.all()
    for user in users:
        key = generate_cache_key(user)
        cache.delete(key)
