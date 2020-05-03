from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField

from products.models import Product

from cities_light.models import City



class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

def __str__(self):
    return self.name


class CartItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return f'{self.quantity} of {self.product.title}'
    
    def get_total_item_price(self):
        return self.quantity * self.product.price
    
    def get_total_item_discount_price(self):
        return self.quantity * self.product.discount_price
    
    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_item_discount_price()
   
    def get_final_price(self):
        if self.product.discount_price:
            return self.get_total_item_discount_price()
        return self.get_total_item_price()


class Cart(models.Model):
    customer = models.ForeignKey('Customer',on_delete=models.CASCADE,null=True,blank=True)
    cartitem = models.ManyToManyField(CartItem)
    total = models.DecimalField(max_digits=100,decimal_places=2,default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    active = models.BooleanField(default=True)
    ordered = models.BooleanField(default=False)
    shipping_adress = models.ForeignKey('Adress',on_delete=models.CASCADE,blank=True,null=True,related_name='shipping_adress')
    billing_adress = models.ForeignKey('Adress',on_delete=models.CASCADE,blank=True,null=True,related_name='billing_adress')
    

    def __str__(self):
        return f'{self.id}'
    

    def get_total(self):
        total = 0
        for cart_item in self.cartitem.all():
            total += cart_item.get_final_price()
        return total  
    
    def total_qantity(self):
        totalQunratity = 0
        for cart_item in self.cartitem.all():
            totalQunratity += cart_item.quantity
        return totalQunratity


ADRESS_FIELDS = (
    ('B','Billing'),
    ('S', 'Shipping')
)


class Adress(models.Model):
    customer = models.ForeignKey('Customer',on_delete=models.CASCADE)
    street_adress = models.CharField(max_length=100)
    apartment_adress = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    city = models.ForeignKey(City,on_delete=models.CASCADE,blank=True, null=True)
    zip_code = models.CharField(max_length=100)
    adress_type = models.CharField(choices=ADRESS_FIELDS,max_length=1)

    class Meta:
        verbose_name_plural = 'Adresses'


