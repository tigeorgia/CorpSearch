from django.contrib import admin
from .models import BannedUser


class BannedUserAdmin(admin.ModelAdmin):
    list_display = ('ip', 'ban_time')


admin.site.register(BannedUser, BannedUserAdmin)

