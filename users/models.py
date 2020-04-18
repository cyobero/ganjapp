from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    PROFILE_TYPE_CHOICES = (
        ('D', 'Driver'),
        ('B', 'Buyer'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=300, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_type = models.CharField(max_length=1, choices=PROFILE_TYPE_CHOICES,
                                    default='B')

    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")
