from django import forms
from .models import Livros, Categoria, Emprestimos


## ('nome', 'autor', 'editora', 'data_cadastro', 'emprestado', 'categoria') 

class CadastroLivro(forms.ModelForm):
    class Meta:
        model = Livros
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].widget = forms.HiddenInput()

class CadastroCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = "__all__"

    def __str__(self):
        return self.nome


class CadastroEmprestimos(forms.ModelForm):
    class Meta:
        model = Emprestimos
        fields = "__all__"

    def __str__(self):
        return f"{self.usuario_emprestado} | {self.livro}"

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimos
        fields = "__all__"

