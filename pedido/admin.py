from django.contrib import admin
from . import models
# Register your models here.


class Item_pedido_inline(admin.TabularInline):
    model = models.ItemPedido
    extra = 1


class Pedido_admin(admin.ModelAdmin):
    inlines = [
        Item_pedido_inline
    ]


admin.site.register(models.Pedido, Pedido_admin)
admin.site.register(models.ItemPedido)
