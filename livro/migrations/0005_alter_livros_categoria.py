# Generated by Django 5.1 on 2024-08-18 13:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0004_categoria_livros_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='livro.categoria'),
        ),
    ]
