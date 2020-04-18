from django.db import models

# Create your models here.
class Dispensary(models.Model):
    name = models.CharField(max_length=100)
    address_one = models.CharField(max_length=100, blank=True, null=True)
    address_two = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    primary_phone = models.IntegerField(max_length=12, blank=True, null=True)
    website = models.URLField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Dispensary", )
        verbose_name_plural = ("Dispensaries")
