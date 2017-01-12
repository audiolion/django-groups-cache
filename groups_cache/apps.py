# -*- coding: utf-8
from django.apps import AppConfig


class GroupsCacheConfig(AppConfig):
    name = 'groups_cache'
    verbose_name = 'Groups Cache'
    verbose_name_plural = 'Groups Cache'

    def ready(self):
        from . import signals
