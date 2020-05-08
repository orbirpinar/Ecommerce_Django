from django.urls import path,include

from .views import viewcart,add_to_cart,remove_from_cart,remove_single_item_from_cart,checkout

urlpatterns = [
    path('',viewcart,name="cart-view"),
    path('add/<slug>',add_to_cart,name="add_to_cart"),
    path('remove/<slug>',remove_from_cart,name="remove_from_cart"),
    path('remove_singe_item/<slug>',remove_single_item_from_cart,name="remove_single_item_from_cart") ,
    path('checkout',checkout,name="checkout")
]
