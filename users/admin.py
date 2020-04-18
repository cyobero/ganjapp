from django.contrib import admin

# Register your models here.
from users.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'birth_date', 'profile_type', )

admin.site.register(Profile, ProfileAdmin)
