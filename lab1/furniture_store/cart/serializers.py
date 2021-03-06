from rest_framework import serializers
from cart.models import Order, OrderItem, Cart, CartItem


class OrderSerializer(serializers.ModelSerializer):
	user = serializers.ReadOnlyField(source='user.id')

	class Meta:
		model = Order
		fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrderItem
		fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cart
		fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
	cart = serializers.ReadOnlyField(source='cart.id')

	class Meta:
		model = CartItem
		fields = '__all__'


class CartItemPUTSerializer(serializers.ModelSerializer):
	cart = serializers.ReadOnlyField(source='cart.id')
	product = serializers.ReadOnlyField(source='product.id')

	class Meta:
		model = CartItem
		fields = '__all__'
