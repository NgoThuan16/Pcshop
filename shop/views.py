from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

def index(request):
    return render(request, "shop/index.html");

def about(request):
    return render(request, "shop/about.html")
