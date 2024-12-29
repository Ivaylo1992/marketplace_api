from django.urls import path

from marketplace_api.api import views

urlpatterns = (
    path('products/', views.ProductListApiView.as_view(), name='product_list'),
    path('products/info/', views.product_info),
    path('products/<int:pk>/', views.ProductDetailApiView.as_view(), name='product_detail'),
    path('orders/', views.OrderListApiView.as_view(), name='order_list'),
    path('user-orders/', views.UserOrderListApiView.as_view(), name='user_order_list'),
)