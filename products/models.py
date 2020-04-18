from django.db import models


FLOWER_KIND_CHOICES = (
    ('S', "Sativa"),
    ('I', 'Indica'),
    ('H', 'Hybrid'),
)

# Create your models here.
class Flower(models.Model):
    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=1, choices=FLOWER_KIND_CHOICES,
                            default='H')
    thc = models.DecimalField(max_digits=2, decimal_places=2, blank=True,
                              null=True)
    cbd = models.DecimalField(max_digits=2, decimal_places=2, blank=True,
                              null=True)
    description = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        verbose_name = ("Flower")
        verbose_name_plural = ("Flowers")
