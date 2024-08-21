from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=40)
    email = models.CharField(max_length=70)
    senha = models.CharField(max_length=64)
    ativo = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


