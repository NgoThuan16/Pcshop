from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"[{self.name}-{self.price}]"

    def image_url(self):
        return f"images\category\products\product_{self.id}.jpg"