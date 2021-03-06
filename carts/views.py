from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect,get_object_or_404
from django.urls import reverse
from django.shortcuts import redirect
from products.models import Product
from django.contrib import messages
from django.http import JsonResponse


from .models import Cart,CartItem
from .forms import AdressForm,CustomerForm

def viewcart(request):
    try:
        the_id = request.session['cart_id']
    except:
        the_id= None
    if the_id:
        cart = Cart.objects.get(id=the_id)
        context = {'cart':cart}
    else:
        context = {'empty':True}
    request.session['total_items'] = cart.total_qantity()
    template = 'carts/view.html'
    return render(request, template,context)

def add_to_cart(request,slug):
    request.session.set_expiry(50000)
    try:
        the_id = request.session['cart_id']
    except:
        new_cart  = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id    
    cart  = Cart.objects.filter(id=the_id)  
   
    isCartInTheProduct = False
    totalItems =cart[0].total_qantity()+1
    product = get_object_or_404(Product,slug=request.GET.get('slug')) 
    cart_item , created = CartItem.objects.get_or_create(product=product)

    if cart.exists():
        order = cart[0]
        if order.cartitem.filter(product__slug=product.slug).exists():
            
            cart_item.quantity+=1
            cart_item.save()
            isCartInTheProduct = True
            return JsonResponse({'isCartInTheProduct':isCartInTheProduct,'quantity':cart_item.quantity,'product_item':product.slug,'totalItems':totalItems})
        else:
            isCartInTheProduct = True
            order.cartitem.add(cart_item)
            return JsonResponse({'isCartInTheProduct':isCartInTheProduct,'product_item':product.slug,'totalItems':totalItems})
    else:
        
        order = Cart.objects.create(id=the_id)
        order.items.add(cart_item)
        isCartInTheProduct = True
        return JsonResponse({'isCartInTheProduct':isCartInTheProduct,'product_item':product.slug,'totalItems':totalItems})

def remove_from_cart(request,slug):
    request.session.set_expiry(50000)
    try:
        the_id = request.session['cart_id']
    except:
        new_cart  = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    
    cart  = Cart.objects.filter(id=the_id)   
    product = get_object_or_404(Product,slug=slug)
    
    if cart.exists():
        order = cart[0]
        if order.cartitem.filter(product__slug=product.slug).exists():
            cart_item = CartItem.objects.filter(product=product)[0]
            order.cartitem.remove(cart_item)
            cart_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect('cart-view')
        else:
            messages.info(request, "This item was not in your cart")
            return redirect('cart-view')
        
    else:
        return redirect("cart-view")
    

def remove_single_item_from_cart(request,slug):
    request.session.set_expiry(50000)
    try:
        the_id = request.session['cart_id']
    except:
        new_cart  = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    
    cart  = Cart.objects.filter(id=the_id)   
    product = get_object_or_404(Product,slug=slug)
    totalItems =cart[0].total_qantity()-1
    if cart.exists():
        order = cart[0]
        if order.cartitem.filter(product__slug=product.slug).exists():
            cart_item = CartItem.objects.filter(product=product)[0]
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
                
                
            elif cart_item.quantity==1:
                print(cart_item)
                order.cartitem.remove(cart_item)
                cart_item.delete()
               
                
            messages.info(request, "This item quantity was updated.")
            return JsonResponse({'quantity':cart_item.quantity,'slug':product.slug,'totalItems':totalItems})
        else:
            messages.info(request, "This item was not in your cart")
            return redirect('cart-view')
        
    else:
        return redirect("cart-view")
    



def checkout(request):
    try:
        the_id = request.session['cart_id']
    except:
        the_id= None
    if the_id:
        cart = Cart.objects.get(id=the_id)
    else:
         messages.info(request, "Your cart is empty")
         return redirect('home')
    if request.method == "POST":
        form = AdressForm(request.POST)
        c_form = CustomerForm(request.POST)
        if form.is_valid():
            adress = form.save(commit=False)
            customer = c_form.save(commit=False)
            if request.user:
                adress.customer = request.user
                adress.save()
                cart.shipping_adress = adress

            adress.save()
            cart.shipping_adress = adress
    else:
        form = AdressForm()

    context = {
        'cart':cart,
        'form':form
    }
    template_name = 'carts/checkout.html'
    return render(request,template_name,context)