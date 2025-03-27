from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem

def index(request):
    return render(request, "shop/index.html")

def about(request):
    return render(request, "shop/about.html")

def services(request):
    products =  Product.objects.all()
    return render(request, "shop/products_category.html", {
        "products": products,
    })

def product(request, product_id):
    _product= Product.objects.get(pk=product_id)
    return render(request, "shop/product.html", {
        "product": _product,
    })

def contact_view(request):
    return render(request, "shop/contact.html")

@login_required
def addToCart(request, product_id):
    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 1))
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, item_created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity}
        )
        if not item_created:
            cart_item.quantity += quantity
            cart_item.save()
    return redirect('product', product_id=product.id)