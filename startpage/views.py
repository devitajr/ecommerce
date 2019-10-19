from django.shortcuts import render
from .models import *
from products.models import *

# Create your views here.

def maisComprados(request):
    pass

def novosProdutos(request):
    pass

def promocao(request):
    pass

def paginaInicial(request):
    
    company = Company.objects.filter()

    carrosel_products = Product.objects.filter(inCarrossel=True)

    items = Product.objects.filter(mostBought=True)

    categories = Category.objects.all()

    return render(request, 'startpage/EntrancePageText.html',{
        'company': company[0],
        'items': items,
        'carrosel_products':carrosel_products,
        'categories': categories,
    })