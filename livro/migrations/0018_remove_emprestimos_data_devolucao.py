# Generated by Django 5.1 on 2024-08-20 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0017_remove_emprestimos_livro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimos',
            name='data_devolucao',
        ),
    ]
