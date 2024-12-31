from django.db.models import Max
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics as api_views
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from marketplace_api.api.filters import (InStockFilterBackend, OrderFilter,
                                         ProductFilter)
from marketplace_api.api.models import Order, Product
from marketplace_api.api.serializers import (OrderSerializer,
                                             ProductInfoSerializer,
                                             ProductSerializer)


class ProductListCreateAPIView(api_views.ListCreateAPIView):
    queryset = Product.objects.all().order_by('pk')
    serializer_class = ProductSerializer

    filterset_class = ProductFilter
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
        InStockFilterBackend,
    )

    search_fields = ('name', 'description')
    ordering_fields = ('name', 'price', 'stock')

    pagination_class = LimitOffsetPagination

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


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer
    permission_classes = (AllowAny, )
    filterset_class = OrderFilter
    filter_backends = (DjangoFilterBackend, )

# class OrderListAPIView(api_views.ListAPIView):
#     queryset = Order.objects.prefetch_related('items__product')
#     serializer_class = OrderSerializer


# class UserOrderListAPIView(api_views.ListAPIView):
#     queryset = Order.objects.prefetch_related('items__product')
#     serializer_class = OrderSerializer
#     permission_classes = (
#         IsAuthenticated,
#     )

#     def get_queryset(self):
#         user = self.request.user
#         qs = super().get_queryset()
#         return qs.filter(user=user)


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