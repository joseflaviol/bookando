import json

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def perfil_logado(request):
    if request.user.is_authenticated:
        return request.user
    return None

def index(request):
    return render(request, "index.html", {"perfil_logado": perfil_logado(request)})

def ver_mais(request):
    return render(request, "ver_mais.html", {"perfil_logado": perfil_logado(request)})

def cadastro(request):
    dados = json.loads(request.body)
    primeiroNome = dados['primeiroNome']
    segundoNome = dados['segundoNome']
    nomeUsuario = dados['nomeUsuario']
    email = dados['email']
    senha = dados['senha']

    if User.objects.filter(username=nomeUsuario):
        return JsonResponse({'ok': False, 'msg': 'Nome de Usuário já cadastrado'})

    if User.objects.filter(email=email):
        return JsonResponse({'ok': False, 'msg': 'Email já cadastrado'})

    user = User.objects.create_user(nomeUsuario, email, senha)
    user.first_name = primeiroNome
    user.last_name = segundoNome
    user.save()

    login(request, user)

    return JsonResponse({'ok': True})

def login_function(request):
    dados = json.loads(request.body)
    nomeUsuario = dados['nomeUsuario']
    senha = dados['senha']
 
    user = authenticate(request, username=nomeUsuario, password=senha)

    if user is not None:
        login(request, user)
        return JsonResponse({'ok': True})
    else:
        return JsonResponse({'ok': False, 'msg': 'Nome de Usuário e/ou senha incorretos'})   

def logout_function(request):
    logout(request)
    return redirect("index")