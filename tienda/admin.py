from django.contrib import admin
from tienda.models import Cliente, Pedido

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'telefono', 'direccion')
    search_fields = ('nombre', 'correo', 'telefono')
    list_filter = ('nombre',)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'nombre', 'descripcion', 'fecha', 'entregado', 'total')
    search_fields = ('cliente__nombre', 'nombre', 'descripcion')
    list_filter = ('fecha', 'entregado')
