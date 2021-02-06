from rest_framework import permissions
from cart.models import Cart, Order


class HasAccessToObject(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.user == obj.user:
			return True
		return False


class IsUserCart(permissions.BasePermission):
	def has_permission(self, request, view):
		if request.user == Cart.objects.get(id=view.kwargs['pk']).user:
			return True
		return False


class IsUserCartItem(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.user == obj.cart.user:
			return True
		return False


class IsUserOrderItem(permissions.BasePermission):
	def has_permission(self, request, view):
		if request.user == Order.objects.get(id=view.kwargs['pk']).user: #obj.order.user:
			return True
		return False


class IsUserOrderItemDetail(permissions.BasePermission):
	def has_permission(self, request, view):
		if request.user == Order.objects.get(id=view.kwargs['o_k']).user:
			return True
		return False
