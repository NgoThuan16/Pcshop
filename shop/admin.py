from django.contrib import admin
from .models import Product, Cart, CartItem
from user.models import userProfile
# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(userProfile)
