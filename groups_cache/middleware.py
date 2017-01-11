from django.conf import settings
from django.http import HttpResponse

from .utils import get_group


class GroupsCacheMiddleware(object):

    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response

    @property
    def lazy_groups(self):
        return get_group(self.user)

    def process_request(self, request):
        self.user = request.user
        request.__class__.my_groups = self.lazy_groups
