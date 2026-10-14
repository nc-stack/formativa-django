from django.contrib import admin
from tienda.models import Cliente, Pedido

admin.site.site_header = "Ventas"
admin.site.site_title = "Ventas"
admin.site.index_title = "Panel de administración de la tienda"

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'telefono', 'direccion')
    search_fields = ('nombre', 'correo', 'telefono')
    list_filter = ('nombre',)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'nombre', 'descripcion', 'fecha', 'entregado', 'total_formateado')
    search_fields = ('cliente__nombre', 'nombre', 'descripcion')
    list_filter = ('fecha', 'entregado')

    @admin.display(description='Total', ordering='total')
    def total_formateado(self, obj):
        return f"${obj.total:,}".replace(',', '.')


