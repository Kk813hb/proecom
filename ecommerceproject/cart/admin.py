from django.contrib.auth import admin
from django.contrib import admin
from .models import Cart, CartItem


class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_id', 'date_added']


admin.site.register(Cart, CartAdmin)


class ProdAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'cart', 'active']
    list_editable = ['quantity']


admin.site.register(CartItem, ProdAdmin)
