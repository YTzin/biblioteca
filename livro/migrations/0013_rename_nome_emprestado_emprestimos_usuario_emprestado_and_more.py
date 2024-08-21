# Generated by Django 5.1 on 2024-08-20 11:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0012_alter_livros_autor_alter_livros_editora_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emprestimos',
            old_name='nome_emprestado',
            new_name='usuario_emprestado',
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='livro',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='livro.livros'),
        ),
    ]
