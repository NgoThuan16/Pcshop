from django.contrib import admin
from .models import Product
from user.models import userProfile
# Register your models here.
admin.site.register(Product)
admin.site.register(userProfile)