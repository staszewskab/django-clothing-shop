from django.urls import path
from .views import ProductListApi, OrderListApi

urlpatterns = [
    path("products/", ProductListApi.as_view(), name="api_products"),
    path("orders/", OrderListApi.as_view(), name="api_orders"),
]