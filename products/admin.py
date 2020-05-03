from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'#zamana göre ürünleri getiriyor
    list_display = ('title','price','active','updated','label','category')
    search_fields = ('title','description',)
    list_editable = ('price','active','label','category')#anlık değişiklik yapılabiliyor çoklu değişiklik
    list_filter = ['price','active']#price ve aktifliğe göre filtre yapabiliyoruz
    readonly_fields = ['updated','timestamp']#sadece okunabilir değiştirilemez
    prepopulated_fields = {"slug": ("title",)}#it means when we type fields also slug is typed at the same time
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
  
