from django.contrib import admin

# Register your models here.
from dispensaries.models import Dispensary

class DispensaryAdmin(admin.ModelAdmin):
    fields = ('name', 'city', 'primary_phone', 'email', 'url', )

admin.site.register(Dispensary, DispensaryAdmin)
