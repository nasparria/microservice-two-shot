from django.contrib import admin
from .models import Location
from .models import Bin


class LocationAdmin(admin.ModelAdmin):
    pass


class BinModel(admin.ModelAdmin):
    pass


admin.site.register(Location, LocationAdmin)
admin.site.register(Bin, BinModel)
