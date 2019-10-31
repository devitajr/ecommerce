from django.db import models
from startpage.models import *
from django.utils.translation import ugettext_lazy as _

# Create your models here

class Product(models.Model):

    name = models.CharField(max_length=150)

    value = models.DecimalField(
        decimal_places = 2,
        max_digits= 11,
    )

    old_value = models.DecimalField(
        decimal_places=2,
        max_digits=11,
    )

    description = models.CharField(max_length=500)

    image_url = models.CharField(max_length=150)

    inPromotion = models.BooleanField(default=False)

    inCarrossel = models.BooleanField(default = False)

    mostBought = models.BooleanField(default = False)

    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING)

    page_url = models.CharField(max_length=500)

    class Meta:
        verbose_name = _("Produto")
        verbose_name_plural = _("Produtos")

    def __str__(self):
        return self.name