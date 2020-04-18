from django.contrib import admin

# Register your models here.
from products.models import Flower

class FlowerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Flower, FlowerAdmin)
