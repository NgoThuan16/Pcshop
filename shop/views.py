from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .models import Product

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