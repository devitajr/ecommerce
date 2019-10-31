from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Company(models.Model):

    name = models.CharField(max_length=150)

    company_logo_url = models.CharField(max_length=300)

    company_telephone = models.CharField(max_length = 50)

    class Meta:
        verbose_name = _("Minha empresa")
        verbose_name_plural = _("Minhas Empresas")

    def __str__(self):
        return self.name

class Category(models.Model):

    name = models.CharField(max_length = 150)
    
    class Meta:
        verbose_name = _("Minha Categoria")
        verbose_name_plural = _("Minhas Cateogiras")

    def __str__(self):
        return self.name

     