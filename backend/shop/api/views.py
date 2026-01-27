from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from shop.api.serializers import ProductSerializer, OrderSerializer
from shop.models import Product, Order

class ProductListApi(APIView):
    def get(self, request):
        products = Product.objects.filter(available=True)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class OrderListApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        orders = Order.objects.prefetch_related('items__product')
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)