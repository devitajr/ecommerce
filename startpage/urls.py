from django.urls import path
from . import views

urlpatterns = [
    path('', views.paginaInicial,name='paginaInicial'),
    path('novosProdutos', views.novosProdutos,name='novosProdutos'),
    path('maisComprados', views.maisComprados,name='maisComprados'),
    path('promocao', views.promocao,name='promocao')
]