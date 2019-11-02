from django.shortcuts import render, redirect
from .models import Product
from startpage.models import *
from django.http import HttpResponseNotFound
from .cart import Cart
from .forms import PayForm


# Create your views here.

def baseProducts(request):
    return render(request,"products/baseProducts.html")

def listaProdutos(request):
    if request.user.is_authenticated:
        company = Company.objects.all()

        categories = Category.objects.all()

        item_pesquisado = ""

        products = Product.objects.all()

        productNotFound=False

        pesquisou_algo = False

        if request.method == "POST":

            item_pesquisado = request.POST.get('item_pesquisado')

            category_name = request.POST.get('category_name')

            if item_pesquisado != "":
                products = Product.objects.filter(name=item_pesquisado)
                pesquisou_algo = True
                if products.exists()==False:
                    productNotFound = True

            else:
                productNotFound = True
            
            if productNotFound and (category_name != ""):
                searched_category = Category.objects.filter(name = category_name)
                if searched_category.exists():
                    products = Product.objects.filter(category=searched_category[0])
                    productNotFound = False

            if productNotFound:
                products = Product.objects.all()

                

        qntd_resultados_items = products.__len__

        return render(request,"products/productList.html",{
            'products': products,
            'company': company[0],
            'qntd_resultados_items': qntd_resultados_items,
            'item_pesquisado': item_pesquisado,
            'categories': categories,
            'pesquisou_algo':pesquisou_algo,
        })

def produto(request,main_product_id):
    if request.user.is_authenticated:
        if main_product_id != None:

            main_product = Product.objects.filter(id = main_product_id)
            
            if main_product.exists():        
                main_product = main_product[0]
                
                company = Company.objects.all()

                categories = Category.objects.all()

                # number_of_stars=main_product.number_of_stars
                number_of_stars = 3
                # quantity_in_stock = main_product.quantity_in_stock
                quantity_in_stock = 3
                related_items = Product.objects.filter(category=main_product.category)
                
                return render(request,"products/product.html",{
                    'number_of_stars': range(0,number_of_stars),
                    'company': company[0],
                    'categories': categories,
                    'main_product':main_product,
                    'related_items':related_items,
                    'quantity_in_stock': range(1,quantity_in_stock)
                })
            
            else:
                return HttpResponseNotFound ('<h1>Erro 404</h1><h3>Produto não encontrado</h3>')    

    else:
        return HttpResponseNotFound ('<h1>Erro 404</h1><h3>Página não encontrada</h3>')

def cartList(request):
    cart = Cart(request)

    context = {
        'cart':cart,
    }

    return render(request, 'cart/cartList.html', context)

def payCompleted(request):
    return render(request, 'pay/payCompleted.html', {})

def payProducts(request):
    cart = Cart(request)
    value = cart.get_total_value()
    return render(request, 'pay/payProducts.html', {'value':value})

def productBreakdown(request):
    return render(request, 'products/productBreakdown.html', {})


def adicionarProdutoCarrinho(request, main_product_id):
    if request.user.is_authenticated:
        if main_product_id != None:
            product = Product.objects.filter(id = main_product_id)[0]
            cart = Cart(request)

            cart.add(product)
    return redirect("listaDeProdutos")

def payment(request):
    if request.user.is_authenticated:
        if(request.method == 'POST'):
            form = PayForm(request.POST)
            if not form.is_valid():
                return redirect(payCompleted)
        else:
            form = PayForm(initial={'key': 'value'})
    
    return redirect('payProducts')
