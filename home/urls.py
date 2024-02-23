from django.urls import path
from .views import Homepage, Categorypage, Storepage, addtocart, cartpage,  wishpage
urlpatterns = [
    path("",Homepage.as_view(),name="home-page"),
    path("category/", Storepage.as_view(), name="store-page"),
    path("category/<str:category>/<int:offset>",Categorypage.as_view(), name="category-page"),
    path("appendcart/<int:product_id>/", addtocart.as_view(), name="append-cart"),
    path("cart/", cartpage.as_view(), name="cart-page"),
    path("wishlist/", wishpage.as_view(), name="wish-page"),
]
