from django.urls import path

from marketplace_api.api import views
from rest_framework.routers import DefaultRouter

urlpatterns = (
    path('products/', views.ProductListCreateAPIView.as_view(), name='product_list'),
    path('products/info/', views.ProductInfoAPIView.as_view(), name='product_info'),
    path('products/<int:product_id>/', views.ProductDetailAPIView.as_view(), name='product_detail'),
)

rauter = DefaultRouter()
rauter.register('orders', views.OrderViewSet)
urlpatterns += tuple(rauter.urls)