from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("services", views.services, name="services"),
    path("contact", views.contact_view, name="contact"),
    path("cart", views.cart_view, name="cart"),
    path("<int:product_id>", views.product, name="product"),
    path("cart/add/<int:product_id>", views.addToCart, name="addToCart"),
    path("cart/remove/<int:id>", views.removeFromCart, name="removeFromCart")
]