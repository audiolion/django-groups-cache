from django.conf import settings
from django.core.cache import cache
from django.core.signals import post_save
from django.dispatch import receiver

from .utils import generate_cache_key


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def invalidate_user_cache(sender, **kwargs):
    key = generate_cache_key(kwargs.get('instance'))
    cache.delete(key)

