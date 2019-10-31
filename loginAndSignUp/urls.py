from django.urls import path
from . import views

urlpatterns = [
    path('entrar', views.entrar,name='entrar'),
    path('seInscreva', views.seInscreva,name='seInscreva'),
    path('baseLoginSignUp', views.base,name='baseLoginSignUp'),
    path('meuPerfil', views.perfil,name='perfil'),
    path('minhasCompras', views.compras,name='compras'),
    path('mudancaDados', views.mudancaDados,name='mudancaDados'),
    path('mudancaSenha', views.mudancaSenha,name='mudancaSenha'),
    path('desativarConta', views.desativarConta,name='desativarConta'),
    path('logout', views.logout_view,name='logout'),
]