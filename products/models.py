from django.db import models


FLOWER_KIND_CHOICES = (
    ('H', 'Hybrid')
    ('I', 'Indica'),
    ('S', 'Sativa')
)

EDIBLE_KIND_CHOICES = (
    ('COOK', 'Cookie'),
    ('GUM', 'Gummy')
    ('CHOC', 'Chocolate'),
    ('O', 'Other'),
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
    quantity = models.DecimalField(max_digits=3, decimal_places=1, blank=True,
                                   null=True, default=0.0)

    class Meta:
        verbose_name = ("Flower")
        verbose_name_plural = ("Flowers")


class PreRoll(models.Model):
    flower = models.OneToOneField(Flower, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Pre-Roll")
        verbose_name = ("Pre-Rolls")


class Cartridge(models.Model):
    flower = models.OneToOneField(Flower, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Cartridge")
        verbose_name = ("Cartridges")


class Edible(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    thc = models.DecimalField(max_digits=2, decimal_places=2, blank=True,
                              null=True, default=0.0)


    class Meta:
        verbose_name = ("Edible")
        verbose_name_plural = ("Edibles")
