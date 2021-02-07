from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProductListView, ProductDetailView, ProductCategoryDetailView,\
    APIProductList, APIProductDetail, api_root, hello


urlpatterns = [
    path('', hello),
    path('api/v1/products/', APIProductList.as_view(), name='product-list'),
    path('api/v1/products/<int:pk>/', APIProductDetail.as_view(), name='product-detail'),
]

#urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('legacy/', ProductListView.as_view(), name='shop-home'),
    path('legacy/category/<int:pk>/', ProductCategoryDetailView.as_view(), name='shop-category'),
    path('legacy/product/<int:pk>/', ProductDetailView.as_view(), name='shop-product')
]
