from django.contrib.auth.models import AbstractUser
from django.db import models
from products.models import Product
from django.utils.translation import ugettext_lazy as _

class CustomUser(AbstractUser):
    
    image_url = models.CharField(
        max_length=200,
        default = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmoOp4gGuNDTJDvGZTJOSNi2B9OCezwVn0gJP--oT3j4LNScNX',
    )

    # cep = models.CharField(
    #     max_length=300,
    # )

    class Meta:
        verbose_name = _("Usuário")
        verbose_name_plural = _("Usuários")

    def __str__(self):
        return self.name


class HistoricoDeCompras(models.Model):

    date = models.DateField()

    product = models.ForeignKey(to="products.Product", on_delete=models.DO_NOTHING)
    
    class Meta:
        verbose_name = _("Compra")
        verbose_name_plural = _("Histórico de Compras")

    def __str__(self):
        return self.date