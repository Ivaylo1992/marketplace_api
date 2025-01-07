from django.db.models import Max
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework import filters
from rest_framework import generics as api_views
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from marketplace_api.api.filters import (InStockFilterBackend, OrderFilter,
                                         ProductFilter)
from marketplace_api.api.models import Order, Product, User
from marketplace_api.api.serializers import (OrderSerializer,
                                             ProductInfoSerializer,
                                             ProductSerializer,
                                             OrderCreateSerializer, UserSerializer)


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
    permission_classes = (IsAuthenticated, )
    filterset_class = OrderFilter
    filter_backends = (DjangoFilterBackend, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return OrderCreateSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(user=self.request.user)
        return qs	

    @action(detail=False, methods=['get'], url_path='user_orders')
    def user_orders(self, request):
        orders = self.get_queryset().filter(user=request.user)
        serializer = self.get_serializer(orders, many=True)

        return Response(serializer.data)


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
    

class UserListView(api_views.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = None