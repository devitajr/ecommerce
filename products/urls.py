from django.urls import path
from . import views

urlpatterns = [
    path('baseProducts', views.baseProducts, name='baseProducts'),
    path('listaDeProdutos', views.listaProdutos, name='listaDeProdutos'),
    path('produto', views.produto, name='produto'),
]