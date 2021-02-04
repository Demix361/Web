from rest_framework import serializers
from cart.models import Order
from django.contrib.auth.models import User


class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = '__all__'
