# Generated by Django 5.1 on 2024-08-19 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0011_alter_livros_emprestado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='autor',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='livros',
            name='editora',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='livros',
            name='nome',
            field=models.CharField(max_length=70),
        ),
    ]
