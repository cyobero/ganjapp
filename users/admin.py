from django.contrib import admin

# Register your models here.
from users.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    fields = ('username', )

admin.site.register(Profile, ProfileAdmin)
