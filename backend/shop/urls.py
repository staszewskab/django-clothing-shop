from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/add/', views.product_add, name='product_add'),
    path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
]