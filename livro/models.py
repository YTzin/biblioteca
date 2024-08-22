from django.db import models
from datetime import date
from usuarios.models import Usuario ##########
from django.core.exceptions import ValidationError


# Create your models here.

class Categoria(models.Model):
    nome =models.CharField(max_length=30)
    descricao = models.TextField(max_length=300)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome

class Livros(models.Model):
    img = models.ImageField(upload_to='capa_livro', null=True, blank=True)
    nome = models.CharField(max_length=70)
    autor = models.CharField(max_length=60)
    editora = models.CharField(max_length=30)
    data_cadastro = models.DateField(default= date.today)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, default=1)
    pdf = models.FileField(upload_to='pdf', null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, null=True, blank=True)

    def clean(self):
        super().clean()
        if not self.nome:
            raise ValidationError('O campo nome não pode ser vazio.')

    class Meta:
        verbose_name = 'Livro'

    def __str__(self):
        return self.nome
    


class Emprestimos(models.Model):
      pass ## implementar sistema de emprestimos



