from django.core.cache import cache
from django.contrib.auth.models import AnonymousUser, User, Group
from django.http import HttpRequest
from django.test import TestCase

from groups_cache.utils import generate_cache_key, cache_groups
from groups_cache import signals
from groups_cache.templatetags.has_group import has_group


class TestHasGroup(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('test', 'test@example.com', 'test_password')
        try:
            self.client.force_login(self.user)
        except AttributeError:
            pass
        self.request = HttpRequest()
        self.request.session = self.client.session
        self.request.user = self.user
        self.group = Group.objects.create(name='nummy')
        self.user.groups.add(self.group)
        self.user.save()

    def test_should_find_nummy_group(self):
        groups = cache_groups(self.user)
        self.assertEqual(len(groups), 1)
        self.assertIs(has_group(self.user, self.group.name), True)
        cache.clear()
        self.assertIs(has_group(self.user, self.group.name), False)

    def test_should_not_find_rocks_group(self):
        groups = cache_groups(self.user)
        self.assertEqual(len(groups), 1)
        self.assertFalse(has_group(self.user, 'rocks'))
        cache.clear()
        self.assertFalse(has_group(self.user, 'rocks'))

    def test_should_return_false_anonymous(self):
        anon = AnonymousUser()
        self.assertFalse(has_group(anon, 'nummy'))
