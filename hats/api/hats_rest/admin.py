from django.contrib import admin

from .models import Hat


class HatAdmin(admin.ModelAdmin):
    pass


admin.site.register(Hat, HatAdmin)