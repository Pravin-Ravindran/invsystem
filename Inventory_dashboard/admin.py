from django.contrib import admin

from .models import Product

from .models import Order
# class created for Admin to display with mentioned fields and holding a filter option.
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','category','quantity','expirydate',)
    list_filter=['category']
# Registered models for Admin
admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
admin.site.site_header='Sr Inventory Dashboard'