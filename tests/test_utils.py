from django.core.cache import cache
from django.contrib.auth.models import AnonymousUser, User, Group
from django.http import HttpRequest
from django.test import TestCase

from groups_cache.utils import generate_cache_key, cache_groups
from groups_cache import signals


class TestCacheGroups(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('test_user2', 'test2@example.com', 'test_password2')
        self.client.force_login(self.user)
        self.request = HttpRequest()
        self.request.session = self.client.session
        self.request.user = self.user
        self.group = Group.objects.create(name='nummy')
        self.user.groups.add(self.group)
        self.user.save()

    def test_cache_invalidates_on_user_save(self):
        groups = cache_groups(self.user)
        self.assertEqual(len(groups), 1)
        self.user.set_password('new_password')
        self.user.save()
        key = generate_cache_key(self.user)
        self.assertIsNone(cache.get(key))
        cache.clear()

    def test_cache_invalidates_on_user_groups_removal(self):
        groups = cache_groups(self.user)
        self.assertEqual(len(groups), 1)
        self.user.groups.remove(self.group)
        self.user.save()
        key = generate_cache_key(self.user)
        self.assertIsNone(cache.get(key))
        cache.clear()

    def test_cache_invalidates_on_group_user_set_removal(self):
        groups = cache_groups(self.user)
        self.assertEqual(len(groups), 1)
        self.group.user_set.remove(self.user)
        self.group.save()
        self.assertEqual(len(self.group.user_set.all()), 0)
        key = generate_cache_key(self.user)
        self.assertIsNone(cache.get(key))
        cache.clear()

    def test_cache_invalidates_on_group_save(self):
        groups = cache_groups(self.user)
        self.assertEqual(len(groups), 1)
        self.group.name = 'dragonlord_ojutai'
        self.group.save()
        self.assertEqual(self.group.name, 'dragonlord_ojutai')
        key = generate_cache_key(self.user)
        self.assertIsNone(cache.get(key))
        cache.clear()
