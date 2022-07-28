from django.contrib import admin

from .models import Bin

# Register your models here.

class BinModel(admin.ModelAdmin):
    pass

admin.site.register(Bin, BinModel)