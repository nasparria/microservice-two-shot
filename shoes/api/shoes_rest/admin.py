from django.contrib import admin

from .models import Shoe, BinVO

# Register your models here.
class ShoeAdmin(admin.ModelAdmin):
    pass

class BinVOAdmin(admin.ModelAdmin):
    pass


admin.site.register(Shoe, ShoeAdmin),
admin.site.register(BinVO, BinVOAdmin)