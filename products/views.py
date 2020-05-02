from django.shortcuts import render

from django.views.generic import ListView
from .models import Product
from django.db.models import Q

def home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,"products/home.html",context)

def productlist(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,"products/product_list.html",context)

def productdetail(request,slug):
    product = Product.objects.get(slug=slug)
    images = product.productimage_set.all()
    context= {'product':product,'images':images}
    return render(request,'products/product_detail.html',context)


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
