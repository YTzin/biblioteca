from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Livros, Categoria
from .forms import CadastroLivro, CadastroCategoria

def home(request):
    if request.session.get('usuario'):
        usuario_id = request.session['usuario']
        try:
            usuario = Usuario.objects.get(id=usuario_id)
            status_categoria = request.GET.get('status_categoria')
            livros = Livros.objects.filter(usuario=usuario)
            form_livro = CadastroLivro()
            form_livro.fields['usuario'].initial = request.session['usuario']
            form_livro.fields['categoria'].queryset = Categoria.objects.filter(usuario=usuario)

            form_categoria = CadastroCategoria()

            return render(request, 'home.html', {
                'livros': livros,
                'usuario_logado': request.session.get('usuario'),
                'form_livro': form_livro,
                'form_categoria': form_categoria,
                'status_categoria': status_categoria,
            })
        except Usuario.DoesNotExist:
            return redirect('/auth/login/?status=2')
    else:
        return redirect('/auth/login/?status=2')


def ver_livros(request, id):
    if request.session.get('usuario'):
        livros = Livros.objects.get(id=id)  
        usuario_id = request.session['usuario']
        if request.session.get('usuario') == livros.usuario.id:
            usuario = Usuario.objects.get(id=usuario_id)
            form = CadastroLivro()
            form.fields['usuario'].initial = request.session['usuario']
            form.fields['categoria'].queryset = Categoria.objects.filter(usuario=usuario)
            return render(request, 'ver_livro.html',  {
                'livro': livros,
                'form': form,
                'usuario_logado': request.session.get('usuario'),
                'id_livro': id,
                'exibir_botoes': False
            })
        else:
            return HttpResponse('Esse livro não é seu') 
    return redirect('/auth/login/?status=2')


def cadastrar_livro(request):
    if request.method == 'POST':
        form = CadastroLivro(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Livro cadastrado com sucesso!')
            return redirect('/livro/home')
        else:
            form_categoria = CadastroCategoria()
            return render(request, 'home.html', {
                'form_livro': form,
                'form_categoria': form_categoria,
                'usuario_logado': True
            })
    else:
        form = CadastroLivro()
        return render(request, 'home.html', {'form': form, 'usuario_logado': True})


def excluir_livro(request, id):
    Livros.objects.get(id=id).delete()
    messages.success(request, 'Livro excluído com sucesso!')
    return redirect('/livro/home')


def cadastrar_categoria(request):
    if request.method == 'POST':
        form = CadastroCategoria(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria cadastrada com sucesso!')
            return redirect('/livro/home')
        else:
            form_livro = CadastroLivro()
            return render(request, 'home.html', {
                'form_livro': form_livro,
                'form_categoria': form,
                'usuario_logado': True
            })
    else:
        form = CadastroCategoria()
        return render(request, 'home.html',  {'form': form})

