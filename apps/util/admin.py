from django.contrib import admin
from .models import BannedUser


class BannedUserAdmin(admin.ModelAdmin):
    list_display = ('ip', 'ban_time', 'tried_to_access')
    readonly_fields = ('tried_to_access',)


admin.site.register(BannedUser, BannedUserAdmin)

