from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.messages.api import success
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order, CartItem, OrderItem
from .forms import ProductForm, RegisterForm
from django.contrib.auth import login
from django.contrib import messages

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer, OrderSerializer
from .models import Product, Order

def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

@staff_member_required
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'shop/product_form.html', {'form': form})

@staff_member_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'shop/product_form.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})

@login_required
def add_to_cart(request,product_id):
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity',1))

    cart_item, created = CartItem.objects.get_or_create(user=request.user ,product=product)

    if not created:
        current_quantity = cart_item.quantity
    else:
        current_quantity = 0
    new_quantity = quantity + current_quantity

    if new_quantity >= product.stock:
        cart_item.quantity = product.stock
        message = f"Maximum available quantity for {product.name} is {product.stock}."
        success = False
    else:
        cart_item.quantity = new_quantity
        message = f"{product.name} added to cart."
        success = True
    cart_item.save()

    return JsonResponse({'success': success, 'quantity': cart_item.quantity, 'message': message})

@login_required
def cart_detail(request):
    cart_items = request.user.cart_items.select_related('product')
    total = sum(item.total_price for item in cart_items)

    if request.method == 'POST':
        if not cart_items.exists():
            return render(request, 'shop/cart.html',
                          {'cart_items': cart_items, 'total': total,
                           'error': 'Your cart is empty!'})

        insufficient_stock_items = []

        with transaction.atomic():
            for item in cart_items:
                if item.quantity > item.product.stock:
                    insufficient_stock_items.append(item.product.name)
                    item.delete()

            if insufficient_stock_items:
                return render(request, 'shop/cart.html',
                      {'cart_items': request.user.cart_items.select_related('product'),
                       'total': sum(item.quantity for item in request.user.cart_items.select_related('product')),
                       'error': f"Not enough stock for: {','.join(insufficient_stock_items)}. These items were removed from your cart."})

            order = Order.objects.create(user=request.user)
            for item in cart_items:
                OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
                item.product.stock -= item.quantity
                item.product.available = item.product.stock > 0
                item.product.save()

            cart_items.delete()

        return redirect('orders_list')

    return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total': total})


@login_required
def orders_list(request):
    orders = request.user.orders.prefetch_related('items').all()
    return render(request,"shop/orders_list.html", {"orders": orders})



@api_view(['GET'])
def api_products(request):
    products = Product.objects.filter(available=True)
    serializer = ProductSerializer(products, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_orders(request):
    orders = request.user.orders.prefetch_related('items').all()
    serializer = OrderSerializer(orders, many=True, context={'request': request})
    return Response(serializer.data)

