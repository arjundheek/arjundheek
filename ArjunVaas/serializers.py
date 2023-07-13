from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','main_image','image_1','image_2',
                 'try_on_main_image','try_on_image1','try_on_image2', 
                 'is_try_on_main_image_enabled',
                 'is_try_on_image1_enabled',
                 'is_try_on_image2_enabled','price', 'url', 'color', 'type']