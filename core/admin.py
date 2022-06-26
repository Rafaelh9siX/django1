from django.contrib import admin

from .models import Cliente, Produto


class ProdutoAdming(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')

admin.site.register(Produto, ProdutoAdming)
admin.site.register(Cliente, ClienteAdmin)