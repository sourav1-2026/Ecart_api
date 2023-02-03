from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = '__all__'

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name can not be blank")
        if Category.objects.filter(name=value).exists():
            raise serializers.ValidationError("A category with the same name already exists.")
        return value

    def validate_description(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name can not be blank")
        return value
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields = '__all__'

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name can not be blank")
        return value
    
    def validate_description(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name can not be blank")
        return value
    
    
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be a positive number")
        return value


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields = '__all__'
    
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be a positive number")
        return value
    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be a positive number")
        return value