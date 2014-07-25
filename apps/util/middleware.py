from .models import BannedUser
from django.http import HttpResponseForbidden


class IpBanMiddleware(object):
    def process_request(self, request):
        headers = ('REMOTE_ADDR', 'HTTP_X_FORWARDED_FOR', 'HTTP_CLIENT_IP', 'HTTP_X_FORWARDED',
                   'HTTP_X_CLUSTER_CLIENT_IP', 'HTTP_FORWARDED')
        ips = []

        for header in headers:
            if request.META.get(header):
                if "," in request.META[header]:
                    ips.extend(x for x in request.META[header].split(","))
                else:
                    ips.append(request.META[header])

        for ip in ips:
            try:
                banned_user = BannedUser.objects.get(ip__iexact=ip)
            except BannedUser.DoesNotExist:
                banned_user = None

            if banned_user and banned_user.is_banned:
                banned_user.tried_to_access += 1
                banned_user.save()
                return HttpResponseForbidden("403 Forbidden")

        return None