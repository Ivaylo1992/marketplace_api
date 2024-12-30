from django.db.models import Max
from django.shortcuts import get_object_or_404
from marketplace_api.api.serializers import \
ProductSerializer, OrderSerializer, ProductInfoSerializer
from marketplace_api.api.models import Product, Order
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics as api_views
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    AllowAny
    )
from rest_framework.views import APIView
from marketplace_api.api.filters import ProductFilter
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class ProductListCreateAPIView(api_views.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filterset_class = ProductFilter
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )

    search_fields = ('name', 'description')
    ordering_fields = ('name', 'price', 'stock')

    def get_permissions(self):
        self.permission_classes = (AllowAny,)
        if self.request.method == 'POST':
            self.permission_classes = (IsAdminUser,)
        return super().get_permissions()


class ProductDetailAPIView(api_views.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'

    def get_permissions(self):
        self.permission_classes = (AllowAny,)
        if self.request.method in ('PATCH', 'PUT', 'DELETE'):
            self.permission_classes = (IsAdminUser,)
        return super().get_permissions()


class OrderListAPIView(api_views.ListAPIView):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer


class UserOrderListAPIView(api_views.ListAPIView):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer
    permission_classes = (
        IsAuthenticated,
    )

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        return qs.filter(user=user)


class ProductInfoAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductInfoSerializer({
            'products': products,
            'count': len(products),
            'max_price': products.aggregate(
                max_price=Max('price')
            )['max_price']
        })

        return Response(serializer.data)