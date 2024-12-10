from django.shortcuts import render
from django.http import HttpResponse
from usuarios.models import Users
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login, logout
from usuarios.models import Users



# Create your views here.

def logar(request):
    if request.method == "GET":
        return render(request, 'logar.html')
    elif request.method == "POST":
        nome = request.POST.get('login')
        senha = request.POST.get('senha')

        usuario = authenticate(username=nome, password=senha)
        print(f"Usuário autenticado: {usuario}")

        if usuario:
            return HttpResponse('Logado')
        else:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha invalidos')
            return render(request, 'logar.html')


    

def cadastrar(request):
    if request.method == "GET":
        return render(request, 'cadastrar.html')

    elif request.method == "POST":
        nome = request.POST.get('login')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        

        if Users.objects.filter(username=nome).exists():
            messages.add_message(request, constants.ERROR, 'Usuário já existe')
            return render(request, 'cadastrar.html')

        elif senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas devem ser iguais')
            return render(request, 'cadastrar.html')

        else:
            usuario = Users(username=nome)  # Inclui o campo personalizado
            usuario.set_password(senha)
            usuario.save()

            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso!')
            return render(request, 'logar.html')

