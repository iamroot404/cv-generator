from django.contrib import admin
from .models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'is_premium', 'modified_date')



admin.site.register(Product, ProductAdmin)