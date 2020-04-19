from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    PROFILE_TYPE_CHOICES = (
        ('D', 'Driver'),
        ('B', 'Buyer'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, blank=False, null=False,
                                default='stoner_unknown')
    bio = models.TextField(max_length=300, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_type = models.CharField(max_length=1, choices=PROFILE_TYPE_CHOICES,
                                    default='B')
    password2 = models.CharField(max_length=128, blank=True, null=True,
                                        default='')


    def __str__(self):
        return self.username

    def password_confirmed(self):
        return self.user.password == self.password2

    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")
