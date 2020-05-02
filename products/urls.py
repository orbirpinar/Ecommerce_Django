from django.urls import path,include
from .views import home,productlist,productdetail,SearchResultView
urlpatterns = [
    
    # path('',  ProductListView.as_view() ,name="home"),
    path('',home,name="home"),
    path('products', productlist, name="product-list" ),
    path('product/<slug>', productdetail,name="product-detail"),
    path('search/',SearchResultView.as_view(),name="search-result")
]
