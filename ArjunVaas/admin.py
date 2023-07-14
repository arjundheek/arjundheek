from django.contrib import admin

# Register your models here.
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "gender")


admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductDuplicate)
admin.site.register(Tryon)
admin.site.register(Banner)
admin.site.register(Document)
