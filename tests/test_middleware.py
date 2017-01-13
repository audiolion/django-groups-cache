from django.core.cache import cache
from django.contrib.auth.models import AnonymousUser, User, Group
from django.test import TestCase
from mock import Mock
import mock
from groups_cache.middleware import GroupsCacheMiddleware
from groups_cache import signals


class TestMiddleware(TestCase):

    def setUp(self):
        self.gcm = GroupsCacheMiddleware()
        self.request = Mock()
        self.user = Mock(id=123, name='bob')
        self.user.is_authenticated.return_value = True

    def test_request_should_not_cache_anonymous(self):
        self.request.user = Mock()
        self.request.user.is_authenticated.return_value = False
        self.assertEqual(self.gcm.process_request(self.request), None)
        self.assertIsNone(self.request.groups_cache)
        cache.clear()

    def test_request_should_cache_authenticated_user(self):
        self.request.user = self.user
        self.user.groups.all.return_value.values_list.return_value = Group.objects.none()
        self.assertEqual(self.gcm.process_request(self.request), None)
        self.assertIsInstance(self.request.groups_cache, type(Group.objects.none()))
        self.assertEqual(len(self.request.groups_cache), 0)
        cache.clear()

    def test_request_should_cache_one_group(self):
        Group.objects.create(name='revelers')
        self.user.groups.all.return_value.values_list.return_value = Group.objects.all()
        self.request.user = self.user
        self.assertEqual(self.gcm.process_request(self.request), None)
        self.assertIsInstance(self.request.groups_cache, type(Group.objects.none()))
        self.assertEqual(len(self.request.groups_cache), 1)

    def test_request_should_hit_cached_one_group(self):
        self.request.user = self.user
        self.assertEqual(self.gcm.process_request(self.request), None)
        self.assertIsInstance(self.request.groups_cache, type(Group.objects.none()))
        self.assertEqual(len(self.request.groups_cache), 1)
