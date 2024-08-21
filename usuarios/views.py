from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from django.contrib.auth.hashers import make_password, check_password
from django.urls import reverse

def login(request):
    if request.session.get('usuario'):
        return redirect('/livro/home')
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

def cadastro(request):
    if request.session.get('usuario'):
        return redirect('/livro/home')
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})

def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    if not nome.strip() or not email.strip():
        return redirect(reverse('cadastro') + '?status=1')

    if len(senha) < 8:
        return redirect(reverse('cadastro') + '?status=2')

    if Usuario.objects.filter(email=email).exists():
        return redirect(reverse('cadastro') + '?status=3')

    try:
        senha_hashed = make_password(senha)
        Usuario.objects.create(nome=nome, email=email, senha=senha_hashed)
        return redirect(reverse('cadastro') + '?status=4')
    except Exception:
        return redirect(reverse('cadastro') + '?status=5')

def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    try:
        usuario = Usuario.objects.get(email=email)
    except Usuario.DoesNotExist:
        return redirect(reverse('login') + '?status=1')

    if not check_password(senha, usuario.senha):
        return redirect(reverse('login') + '?status=1')

    request.session['usuario'] = usuario.id
    return redirect(f"/livro/home/?id_usuario={request.session['usuario']}")

def sair(request):
    request.session.flush()
    return redirect('/auth/login/')
