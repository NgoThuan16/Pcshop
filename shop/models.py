from django.db import models
from django.conf import settings

class Product(models.Model):
    name = models.CharField(max_length = 200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"[{self.name}-{self.price}]"

    def image_url(self):
        return f"images\category\products\product_{self.id}.jpg"

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart of user: {self.user.id}"
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def Total(self):
        return self.quantity *  self.product.price
