from django.contrib import admin
from .models import Category,Product,Order,OrderItem

@admin.register(Category)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description','price']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at']


@admin.register(OrderItem)
class OrdeItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'quantity', 'price','product']