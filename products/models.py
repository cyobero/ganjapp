from django.db import models


FLOWER_KIND_CHOICES = (
    ('H', 'Hybrid'),
    ('I', 'Indica'),
    ('S', 'Sativa'),
)

FLOWER_QTY_CHOICES = (
    (1.0, '1 gram'),
    (3.5, 'Eighth'),
    (7.0, 'Quarter'),
    (14.0, 'Half'),
    (28.0, 'Ounce')
)

EDIBLE_KIND_CHOICES = (
    ('COOK', 'Cookie'),
    ('GUM', 'Gummy'),
    ('CHOC', 'Chocolate'),
    ('O', 'Other'),
)

# Create your models here.
class Flower(models.Model):
    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=1, choices=FLOWER_KIND_CHOICES,
                            default='H')
    thc = models.DecimalField(max_digits=4, decimal_places=2, blank=True,
                              null=True)
    cbd = models.DecimalField(max_digits=2, decimal_places=2, blank=True,
                              null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    quantity = models.DecimalField(decimal_places=2, max_digits=4, choices=FLOWER_QTY_CHOICES, blank=True,
                                   null=True, default=0.0)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Flower")
        verbose_name_plural = ("Flowers")


class PreRoll(models.Model):
    flower = models.OneToOneField(Flower, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=4, decimal_places=2,
                                   choices=FLOWER_QTY_CHOICES, default=0.0)

    def __unicode__(self):
        return self.flower.name

    def __str__(self):
        return self.flower.name

    class Meta:
        verbose_name = ("Pre-Roll")
        verbose_name_plural = ("Pre-Rolls")


class Cartridge(models.Model):
    flower = models.OneToOneField(Flower, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.flower.name

    class Meta:
        verbose_name = ("Cartridge")
        verbose_name_plural = ("Cartridges")


class Edible(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    thc = models.DecimalField(max_digits=4, decimal_places=2, blank=True,
                              null=True, default=0.0)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = ("Edible")
        verbose_name_plural = ("Edibles")
