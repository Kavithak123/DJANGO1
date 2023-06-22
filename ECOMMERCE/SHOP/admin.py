from django.contrib import admin

from SHOP.models import Category,Product

class Categoryadmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
# Register your models here.

admin.site.register(Category,Categoryadmin)


class Productadmin(admin.ModelAdmin):
    list_display=['name','slug','price','stock','available','created','update']

    prepopulated_fields = {'slug':('name',)}

admin.site.register(Product,Productadmin)