from django.urls import reverse
from django.db import models
from PIL import Image
from django.db.models import Q
from django.contrib.auth.models import User



class ProductImage(models.Model):
        product = models.ForeignKey('Product',on_delete=models.CASCADE)
        image = models.ImageField(upload_to='products/images/')
        featured = models.BooleanField(default=False)
        thumbnail = models.BooleanField(default=False)
        active = models.BooleanField(default=True)
        updated = models.DateTimeField(auto_now_add=False,auto_now=True)

        def __str__(self):
            return self.product.title
        
        def save(self,*args,**kwargs):
            #run to save method parent class
            super().save(*args,**kwargs)
            img = Image.open(self.image.path)
            if  not self.featured:
                output_size = (90,60)
                img.thumbnail(output_size)
                img.save(self.image.path)
            else:
                output_size = (300,300)
                img.thumbnail(output_size)
                img.save(self.image.path)
        


CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('SW', 'Sport wear'),
    ('OW', 'Outwear')
)
LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)



class Product(models.Model):
    title = models.CharField(max_length=120,null=False,blank=False)
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(decimal_places=2,max_digits=100, default=29.99)
    discount_price = models.DecimalField(decimal_places=2,max_digits=100,null=True,blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2,default="S")
    label = models.CharField(choices = LABEL_CHOICES,max_length=1,null=True,blank=True)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    def get_price(self):
        return self.price
    
    class Meta:
        unique_together = ['title','slug']
    
    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"slug": self.slug})
        # return reverse('product-detail',args=[self.slug])
    

    
    """ auto_now_add True ise kaydedildiğinde tarih giriyor
    auto_now False ise update edildiğinde tarihi değiştirmiyor
    o yüzden updated alanında auto_now True oldu """



  



    