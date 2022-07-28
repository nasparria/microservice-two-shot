from django.contrib import admin

from .models import Shoe

# Register your models here.
class ShoeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Shoe, ShoeAdmin)