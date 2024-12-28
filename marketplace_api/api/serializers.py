from rest_framework import serializers
from marketplace_api.api.models import Product, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'name',
            'decription',
            'price',
            'stock',
        )

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                'Price must be greater than 0!'
            )
        return value
    

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'order_id',
            'created_at',
            'user',
            'status'
        )