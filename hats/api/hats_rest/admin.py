from django.contrib import admin

from .models import Hat, LocationVO


class HatAdmin(admin.ModelAdmin):
    pass


class LocationVOAdmin(admin.ModelAdmin):
    pass


admin.site.register(Hat, HatAdmin)
admin.site.register(LocationVO, LocationVOAdmin)