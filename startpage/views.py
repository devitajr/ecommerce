from django.shortcuts import render
from .models import *
from products.models import *
from products.cart import Cart

# Create your views here.

def maisComprados(request):
    return render(request, "startpage/mostBought.html")

def novosProdutos(request):
    return render(request, "startpage/NewProducts.html")

def promocao(request):
    return render(request, "startpage/promotion.html")

def paginaInicial(request):
    
    user = request.user

    company = Company.objects.filter()

    categories = Category.objects.all()

    carrosel_products = Product.objects.filter(inCarrossel=True)

    items = Product.objects.filter(mostBought=True)

    categories = Category.objects.all()

    cart = Cart(request)
    num = cart.__len__()


    print("---------------------")
    print(num)
    print("---------------------")
    return render(request, 'startpage/EntrancePageText.html',{
        'company': company[0],
        'items': items,
        'carrosel_products':carrosel_products,
        'categories': categories,
        'user':user,
        'categories':categories,
        'num':num
    })