from django.db import models
from startpage.models import *

# Create your models here

class Product(models.Model):

    name = models.CharField(max_length=150)

    value = models.DecimalField(
        decimal_places = 2,
        max_digits= 11,
    )

    description = models.CharField(max_length=500)

    image_url = models.CharField(max_length=150)

    inPromotion = models.BooleanField(default=False)

    inCarrossel = models.BooleanField(default = False)

    mostBought = models.BooleanField(default = False)

    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING)