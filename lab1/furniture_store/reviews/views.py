from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from reviews.permissions import CanCreateReview, CanAlterReview
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


class APIReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          CanCreateReview]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user, product=Product.objects.get(id=self.kwargs['pk']))

    def get_queryset(self):
        return Review.objects.filter(product=self.kwargs['pk'])




class APIReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CanAlterReview]




class ReviewCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Review
    fields = ['rating', 'advantages', 'disadvantages', 'review']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.product = Product.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.id in Product.objects.get(id=self.kwargs['pk']).get_reviews().values_list('user', flat=True):
            return False
        if not Product.objects.get(id=self.kwargs['pk']).displayed:
            return False
        return True


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    fields = ['rating', 'advantages', 'disadvantages', 'review']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.product = Product.objects.get(id=self.kwargs['prod'])
        return super().form_valid(form)

    def test_func(self):
        if self.request.user == self.get_object().user:
            return True
        return False


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    success_url = '/'

    def test_func(self):
        if self.request.user == self.get_object().user:
            return True
        return False
