from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ReviewCreateView, ReviewUpdateView, ReviewDeleteView, \
    APIReviewList, APIReviewDetail


urlpatterns = [
    path('shop/<int:pk>/reviews/', APIReviewList.as_view(), name='api-review-list'),
    path('shop/<int:prod>/reviews/<int:pk>/', APIReviewDetail.as_view(), name='api-review-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('legacy/product/<int:pk>/rev-create/', ReviewCreateView.as_view(), name='review-create'),
    path('legacy/product/<int:prod>/<int:pk>/rev-update/', ReviewUpdateView.as_view(), name='review-update'),
    path('legacy/product/<int:prod>/<int:pk>/rev-delete/', ReviewDeleteView.as_view(), name='review-delete'),
]
