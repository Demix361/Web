from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.decorators import method_decorator
from .models import Cart, CartItem, Order, OrderItem
from users.models import MyUser, LoyaltyCard
from shop.models import Product

from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import generics, permissions, renderers
from cart.serializers import OrderSerializer, OrderItemSerializer, CartSerializer, \
    CartItemSerializer, CartItemPUTSerializer
from cart.permissions import HasAccessToObject, IsUserCart, IsUserCartItem, \
    IsUserOrderItem, IsUserOrderItemDetail


# orders/
class APIOrderList(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        if not Cart.objects.get(user=self.request.user).is_empty():
            serializer.save(user=self.request.user)


# (Protected) orders/<pk>/
class APIOrderDetail(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, HasAccessToObject]


# orders/<pk>/orderitems/
class APIOrderItemList(generics.ListAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsUserOrderItem]

    def get_queryset(self):
        return OrderItem.objects.filter(order=self.kwargs['pk'])


# orders/<o_k>/orderitems/<pk>/
class APIOrderItemDetail(generics.RetrieveAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsUserOrderItemDetail]


class APICartDetail(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated, HasAccessToObject]


# (Protected) POST: product, quantity
class APICartItemList(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsUserCart]

    # Нельзя сохранить, если такой товар уже есть в корзине
    def perform_create(self, serializer):
        if len(self.get_queryset().filter(product=self.request.data['product'])) == 0:
            serializer.save(cart=Cart.objects.get(id=self.kwargs['pk']))

    def get_queryset(self):
        return Cart.objects.get(id=self.kwargs['pk']).get_cart_items()


# (Protected) DEL, PUT: quantity
class APICartItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemPUTSerializer
    permission_classes = [permissions.IsAuthenticated, IsUserCartItem]

    def get_queryset(self):
        return CartItem.objects.filter(cart=self.kwargs['c_k'])






class CartListView(LoginRequiredMixin, ListView):
    model = Cart
    template_name = 'cart/cart_list.html'
    context_object_name = 'cart'

    def get_queryset(self):
        return Cart.objects.get(user=self.request.user)


class OrderDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Order
    template_name = 'cart/order_detail.html'
    context_object_name = 'order'

    def test_func(self):
        order = self.get_object()
        if self.request.user == order.user:
            return True
        return False


class OrderCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Order
    fields = ['payment_method', 'address', 'notes']

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user

        # Перемещение в заказ и удаление из корзины - в сигналах
        return super().form_valid(form)

    def test_func(self):
        user = self.request.user
        if Cart.objects.get(user=user).is_empty():
            return False

        # Проверка что товар в наличии и отображается, иначе удаление таких товаров из корзины
        if len(Cart.objects.get(user=user).get_cart_items().filter(product__in_stock=False)) > 0 or \
            len(Cart.objects.get(user=user).get_cart_items().filter(product__displayed=False)) > 0:

            Cart.objects.get(user=user).get_cart_items().filter(product__in_stock=False).delete()
            Cart.objects.get(user=user).get_cart_items().filter(product__displayed=False).delete()

            return False
        return True


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'cart/order_list.html'
    context_object_name = 'orders'
    paginate_by = 12

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-order_time')


@login_required()
def add_to_cart(request, **kwargs):
    product = Product.objects.filter(id=kwargs.get('pk')).first()
    cart = Cart.objects.get(user=request.user)

    if product.id not in cart.cartitem_set.all().values_list('product', flat=True) and product.displayed and product.in_stock:
        new_cart_item = CartItem(cart=cart, product=product)
        new_cart_item.save()
        print('ITEM ADDED TO CART')
    else:
        print('ITEM ALREADY IN CART')

    return redirect(request.META.get('HTTP_REFERER', 'shop-home'))


@login_required()
def remove_from_cart(request, **kwargs):
    product = Product.objects.filter(id=kwargs.get('pk')).first()
    cart = Cart.objects.get(user=request.user)

    if product.id in cart.cartitem_set.all().values_list('product', flat=True):
        CartItem.objects.filter(cart=cart, product=product).delete()
        print('ITEM DELETED')
    else:
        print('ITEM NOT IN CART')

    return redirect(request.META.get('HTTP_REFERER', 'shop-home'))


@login_required()
def increase_quantity(request, **kwargs):
    product = Product.objects.filter(id=kwargs.get('pk')).first()
    cart = Cart.objects.get(user=request.user)

    if product.id in cart.cartitem_set.all().values_list('product', flat=True):
        quantity = CartItem.objects.filter(cart=cart, product=product).first().quantity

        if quantity < 20:
            CartItem.objects.filter(cart=cart, product=product).update(quantity=quantity + 1)
            print('ITEM QUANTITY INCREASED')
        else:
            print('MAXIMUM QUANTITY IS REACHED')
    else:
        print('ITEM NOT IN CART')


    return redirect(request.META.get('HTTP_REFERER', 'shop-home'))


@login_required()
def decrease_quantity(request, **kwargs):
    product = Product.objects.filter(id=kwargs.get('pk')).first()
    cart = Cart.objects.get(user=request.user)

    if product.id in cart.cartitem_set.all().values_list('product', flat=True):
        quantity = CartItem.objects.filter(cart=cart, product=product).first().quantity

        if quantity > 1:
            CartItem.objects.filter(cart=cart, product=product).update(quantity=quantity - 1)
            print('ITEM QUANTITY DECREASED')
        else:
            print('MINIMUM QUANTITY IS REACHED')
    else:
        print('ITEM NOT IN CART')

    return redirect(request.META.get('HTTP_REFERER', 'shop-home'))
