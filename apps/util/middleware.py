from .models import BannedUser
from django.http import HttpResponseForbidden


class IpBanMiddleware(object):
    def __init__(self):
        self.headers = ('REMOTE_ADDR', 'HTTP_X_FORWARDED_FOR', 'HTTP_CLIENT_IP', 'HTTP_X_FORWARDED',
                        'HTTP_X_CLUSTER_CLIENT_IP', 'HTTP_FORWARDED')
        self.ips = []

    def get_banned_user_or_none(self):
        for ip in self.ips:
            try:
                banned_user = BannedUser.objects.get(ip=ip)
            except BannedUser.DoesNotExist:
                banned_user = None

            return banned_user

    def process_request(self, request):
        for header in self.headers:
            if request.META.get(header):
                if isinstance(request.META[header], str):
                    self.ips.append(request.META[header])
                else:
                    self.ips.extend(x for x in request.META[header])

        banned_user = self.get_banned_user_or_none()
        if banned_user and banned_user.is_banned:
                return HttpResponseForbidden("403 Forbidden")
