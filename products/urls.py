from django.urls import path
from . import views

urlpatterns = [
    path('baseProducts', views.baseProducts, name='baseProducts'),
    path('listaDeProdutos', views.listaProdutos, name='listaDeProdutos'),
    path('produto/<int:main_product_id>/', views.produto, name='produto'),
    path('cartList', views.cartList, name='cartList'),
    path('payCompleted', views.payCompleted, name='payCompleted'),
    path('payProduct', views.payProducts, name='payProducts'),
    path('productBreakdown', views.productBreakdown, name='productBreakdown'),
    path('adicionarProdutoCarrinho/<int:main_product_id>/', views.adicionarProdutoCarrinho, name='adicionarProdutoCarrinho'),
    path('payment', views.payment, name='payment'),
]