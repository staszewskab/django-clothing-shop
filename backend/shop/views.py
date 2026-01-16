from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop:product_list')
    else:
        form = ProductForm()
    return render(request, 'shop/product_form.html', {'form': form})

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('shop:product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'shop/product_form.html', {'form': form})