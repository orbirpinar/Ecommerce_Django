from django.contrib import admin
from .models import Cart,CartItem,Adress

class CartAdmin(admin.ModelAdmin):
    class Meta:
        model = Cart

admin.site.register(Cart,CartAdmin)
admin.site.register(CartItem)
admin.site.register(Adress)