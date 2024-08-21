# Generated by Django 5.1 on 2024-08-18 19:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0007_categoria_usuario_alter_livros_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livros',
            name='data_devolucao',
        ),
        migrations.RemoveField(
            model_name='livros',
            name='data_emprestimo',
        ),
        migrations.RemoveField(
            model_name='livros',
            name='nome_emprestado',
        ),
        migrations.CreateModel(
            name='Emprestimos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_emprestado', models.CharField(blank=True, max_length=30, null=True)),
                ('data_emprestimo', models.DateField(blank=True, null=True)),
                ('data_devolucao', models.DateField(blank=True, null=True)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='livro.livros')),
            ],
        ),
    ]
