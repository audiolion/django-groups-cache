from django.conf import settings
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from .utils import get_group


class GroupsMiddleware(MiddlewareMixin):

    @property
    def lazy_groups(self):
        return get_group(self.user)

    def process_request(self, request):
        self.user = request.user
        request.__class__.my_groups = self.lazy_groups
