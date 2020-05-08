from django.shortcuts import render,get_object_or_404
from django.views.generic.detail import BaseDetailView
from django.http import JsonResponse
from django.views.generic import ListView,DetailView


from .models import Product
from carts.models import Cart,CartItem



from django.db.models import Q

def home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,"products/home.html",context)

def productlist(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,"products/product_list.html",context)

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = "products/product_detail.html"



    


class SearchResultView(ListView):
    model = Product
    template_name = 'products/search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q') 
        object_list = Product.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
        return object_list



# class ProductListView(ListView):
#     model = Product
#     template_name = 'products/home.html'
