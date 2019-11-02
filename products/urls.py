from django.urls import path
from . import views

urlpatterns = [
    path('baseProducts', views.baseProducts, name='baseProducts'),
    path('listaDeProdutos', views.listaProdutos, name='listaDeProdutos'),
    path('produto/<int:main_product_id>/', views.produto, name='produto'),
]