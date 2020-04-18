from django.db import models

# Create your models here.
class Flower(models.Model):
    FLOWER_KIND_CHOICES = (
        ("S", "Sativa"),
        ("I", "Indica"),
        ("H", "Hybrid"),
    )
    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=1, choices=FLOWER_KIND_CHOICES)
    thc = models.DecimalField(max_digits=4, decimal_places=2,
                              blank=True, null=True)

    class Meta:
        verbose_name = _("Flower")
        verbose_name_plural = _("Flowers")
