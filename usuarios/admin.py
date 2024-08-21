from usuarios.models import Usuario
from django.contrib import admin

# Register your models here.


@admin.register(Usuario)
class UsurioAdmin(admin.ModelAdmin):
    readonly_fields = ('nome', 'email', 'senha')


