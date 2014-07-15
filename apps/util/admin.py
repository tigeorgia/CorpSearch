from django.contrib import admin
from .models import BannedUser

class BannedUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(BannedUser, BannedUserAdmin)