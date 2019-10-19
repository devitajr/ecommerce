from django.shortcuts import render
from django.contrib.auth import authenticate

# Create your views here.

def entrar(request):
    
    if request.method == "POST":
        username = request.POST['username']

        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, "startpage/EntrancePage.html")

    return render(request, 'loginAndSignUp/login.html')

def seInscreva(request):
    pass