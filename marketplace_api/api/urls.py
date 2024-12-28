from django.urls import path

from marketplace_api.api import views

urlpatterns = (
    path('products/', views.product_list),
    path('products/<int:pk>/', views.product_details),
)