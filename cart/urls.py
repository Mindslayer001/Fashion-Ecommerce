from django.urls import path
from .views import cartpage, wishpage, addtocart
urlpatterns = [
    path("cart/", cartpage, name="cart-page"),
   path("wishlist/", wishpage, name="wish-page"),
   path("appendcart/<int:id>/", addtocart, name="append-cart")
]