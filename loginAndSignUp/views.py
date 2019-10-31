from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from startpage.models import *
from loginAndSignUp.models import CustomUser
from django.contrib.auth.hashers import check_password

def entrar(request):
    
    user_does_not_exist = False

    if request.user.is_authenticated == False:
        company = Company.objects.filter()
        categories = Category.objects.all()
        if request.method == "POST":

            username = request.POST.get('username')

            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("paginaInicial")

            else:
                user_does_not_exist = True


        return render(request, 'loginAndSignUp/login.html',{
            "user_does_not_exist": user_does_not_exist,
            "company": company[0],
            'categories': categories
        })
    
    else:
        return redirect("paginaInicial")


def seInscreva(request):
    
    passwordsNotEqual = False
    
    user = request.user

    company = Company.objects.filter()

    alreadyExistsUser = False

    if user.is_authenticated == False:

        categories = Category.objects.all()

        if request.method == "POST":
            
            first_name = request.POST.get('first_name')

            last_name = request.POST.get('last_name')

            email = request.POST.get('email')

            username = request.POST.get('username')

            password = request.POST.get('password1')

            password2 = request.POST.get('password2')

            possibleAlreadyUser = CustomUser.objects.filter(username=username)

            if possibleAlreadyUser.exists() == False:
                
                newUser = CustomUser(
                    first_name = first_name,
                    last_name = last_name,
                    email = email,
                    username = username,
                    is_superuser = False,
                )

                newUser.set_password(password)

                passwordsNotEqual = True

                if password == password2:
                    passwordsNotEqual = False
                    newUser.save()
                    login(request, newUser)
                    return redirect("paginaInicial")

            else:
                alreadyExistsUser = True

        return render(request, "loginAndSignUp/signUp.html",{
            'company': company[0],
            'passwordsNotEqual': passwordsNotEqual,
            'user': user,
            'alreadyExistsUser':alreadyExistsUser,
            'categories': categories,
        })
    
    else:
        return redirect("paginaInicial")

def perfil(request):

    if request.user.is_authenticated:

        categories = Category.objects.all()
        
        company = Company.objects.filter()

        return render(request, "loginAndSignUp/profile.html",{
            'theads':['Dia da Compra', 'Nome do produto'],
            'trows':[['ontem','banana'],['amanhã','maçã']],
            'company':company[0],
            'categories': categories,
        })
    
    else: 
        return redirect("paginaInicial")

def mudancaDados(request):
    
    if request.user.is_authenticated:

        passwordsEqual = True

        passwordCorrect = True

        company = Company.objects.filter()

        categories = Category.objects.all()

        if request.method == "POST":

            passwordsEqual = False

            passwordCorrect = False
            
            first_name = request.POST.get('first_name')

            last_name = request.POST.get('last_name')

            email = request.POST.get('email')
            
            cep = request.POST.get('cep')

            password = request.POST.get('password')

            password1 = request.POST.get('password1')

            if password == password1:
                passwordsEqual = True
            
            if check_password(password, request.user.password):
                passwordCorrect = True

            if (passwordCorrect and passwordsEqual):
                user = request.user
                user.first_name = first_name
                user.last_name = last_name
                user.email = user.email
                user.cep = cep
                user.save()

        return render(request,"loginAndSignUp/changeData.html",{
            'company': company[0],
            'passwordsEqual': passwordsEqual,
            'passwordCorrect': passwordCorrect,
            'categoires':categories,
        })

    else:
        return redirect("paginaInicial")

def mudancaSenha(request):
    
    if request.user.is_authenticated:
        
        categories = Category.objects.all()

        passwordsDifferent = False

        passwordCorrect = True

        company = Company.objects.filter()

        if request.method == "POST":

            passwordCorrect = False

            password = request.POST.get('password')

            new_password = request.POST.get('new_password')

            new_password1 = request.POST.get('new_password1')

            if check_password(password, request.user.password):
                passwordCorrect = True

            if new_password != new_password1:
                passwordsDifferent = True

            if ((passwordsDifferent==False) and passwordCorrect):
                user = request.user
                user.set_password(new_password)
                user.save()

        return render(request,"loginAndSignUp/changePassword.html",{
            'company':company[0],
            'passwordCorrect':passwordCorrect,
            'passwordsDifferent':passwordsDifferent,
            'categories': categories
        })
    else:
        return redirect("paginaInicial")

def desativarConta(request):
    
    senhaErrada = False

    if request.user.is_authenticated:

        categories = Category.objects.all()

        company = Company.objects.filter()

        if request.method == "POST":
            
            password = request.POST.get('password')

            if check_password(password,request.user.password):
                request.user.delete()

            else:
                senhaErrada = True

            if senhaErrada:
                return render(request,"loginAndSignUp/deleteAccount.html",{
                    'company': company[0],
                    'senhaErrada': senhaErrada,
                    'categories': categories,
                }) 
            
            else:
                return redirect("paginaInicial")
        else:
            return render(request,"loginAndSignUp/deleteAccount.html",{
                    'company': company[0],
                    'senhaErrada': senhaErrada,
                    'categories': categories,
                }) 
    
    else:
        return redirect("paginaInicial")

def logout_view(request):
    
    logout(request)

    return redirect("paginaInicial")


def compras(request):
    pass


def base(request):
    return render(request, "loginAndSignUp/baseLoginAndSignUp.html")