from django.contrib import admin

from broadcast.models import BTopic, BEntry
admin.site.register(BTopic)
admin.site.register(BEntry)
