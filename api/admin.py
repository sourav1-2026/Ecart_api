from django.contrib import admin
from .models import Category,Product,Order,OrderItem
from django.utils.html import format_html


@admin.register(Category)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    #readonly_fields=('photo_tags')
    #fields=('name',) to hide all the field in the admin pannel when we add product from the GUI
    #exclude=('name',) this field hide
    # slug field ---> find the use of it
    #list_display = ['id', 'name', 'short_description','price','image']--> we can use image field as well but we have to set static field
    #radio_fields={"tags":admin.VERTICAL}
    list_display = ['id', 'name', 'short_description','price','click_me',]
    list_display_links=('name','short_description')
    list_filter=('price','created_at')
    

    # since suppose a user type huge description then we must have to handle this case that's why i write short_description 
    def short_description(self,obj):
        return format_html(
            ' <span style="color: #efb80b;">{}</span>',obj.description[:50])
        #return obj.description[:50]

    def click_me(self,obj):
        return format_html(u'<a href="http://127.0.0.1:8000/admin/api/product/{}/change/">{}</a>', 
                               obj.id, "view")

    # def Photo_tag(self,obj):
    #     return format_html(u'<a href="http://127.0.0.1:8000/admin/api/product/{}/change/">{}</a>', 
    #                            obj.id, "view")  use image tage here


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at']


@admin.register(OrderItem)
class OrdeItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'quantity', 'price','product']