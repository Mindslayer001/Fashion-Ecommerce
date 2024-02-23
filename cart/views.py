from django.shortcuts import render
from .models import UserCart, UserWishList
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
# Create your views here.

class cartpage(ListView):
    model = UserCart
    template = "cart/cartpage.html"
    
class wishpage(ListView):
    model = UserWishList
    template = "cart/wishpage.html"
    