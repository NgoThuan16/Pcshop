from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .models import product

def index(request):
    return render(request, "shop/index.html")

def about(request):
    return render(request, "shop/about.html")

def services(request):
    products =  product.objects.all()
    return render(request, "shop/products_category.html", {
        "products": products,
    })