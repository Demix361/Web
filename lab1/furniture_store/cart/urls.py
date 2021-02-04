from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    CartListView,
    add_to_cart,
    remove_from_cart,
    increase_quantity,
    decrease_quantity,
    OrderCreateView,
    OrderListView,
    OrderDetailView,

    APIOrderList,
    APIOrderDetail,
    APICartDetail,
    APICartItemListView,
    APICartItemDetailView
)

urlpatterns = [
    path('orders/', APIOrderList.as_view(), name='api-order-list'),
    path('orders/<int:pk>/', APIOrderDetail.as_view(), name='api-order-detail'),
    path('carts/<int:pk>/', APICartDetail.as_view(), name='api-cart-detail'),
    path('carts/<int:pk>/cartitems/', APICartItemListView.as_view(), name='api-cartitem-list'),
    path('carts/<int:c_k>/cartitems/<int:pk>', APICartItemDetailView.as_view(), name='api-cartitem-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('legacy/cart/', CartListView.as_view(), name='cart'),
    path('legacy/add-to-cart/<int:pk>/', add_to_cart, name="add-to-cart"),
    path('legacy/remove-from-cart/<int:pk>/', remove_from_cart, name="remove-from-cart"),
    path('legacy/increase-quantity/<int:pk>/', increase_quantity, name="increase-quantity"),
    path('legacy/decrease-quantity/<int:pk>/', decrease_quantity, name="decrease-quantity"),
    path('legacy/cart/order/', OrderCreateView.as_view(), name='order-create'),
    path('legacy/orders/', OrderListView.as_view(), name='orders'),
    path('legacy/orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]
