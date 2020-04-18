from django.contrib import admin

# Register your models here.
from products.models import Flower, PreRoll, Cartridge, Edible

class CartridgeAdmin(admin.ModelAdmin):
    pass

class EdibleAdmin(admin.ModelAdmin):
    pass

class FlowerAdmin(admin.ModelAdmin):
    pass

class PreRollAdmin(admin.ModelAdmin):
    pass


admin.site.register(Flower, FlowerAdmin)
admin.site.register(Cartridge, CartridgeAdmin)
admin.site.register(Edible, EdibleAdmin)
admin.site.register(PreRoll, PreRollAdmin)
