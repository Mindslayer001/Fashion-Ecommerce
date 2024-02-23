from django.shortcuts import render,redirect    
from .models import Product, UserCart, UserWishList
from django.views import View
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView

class Homepage(TemplateView):
    template_name = 'home/product_list.html'
    model = Product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Product.objects.values_list('category', flat=True).distinct()
        context["products"] = Product.objects.all()
        context["categories"] = categories
        context["cartitems"] = UserCart.objects.all()
        return context
    
class Categorypage(ListView):
    template_name = 'home/category_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        # Assuming you pass the category id in the URL as 'category_id'
        category = self.kwargs['category']
        offset = self.kwargs['offset']
        context = Product.objects.filter(category=category)
        if len(context) > offset:
            return context[offset:]
        return context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cartitems"] = UserCart.objects.all() 
        return context
    
    
class Storepage(ListView):
    template_name = 'home/category_list.html'
    model = Product 
    context_object_name = 'products'

    
class wishpage(ListView):
    model = UserWishList
    template = "cart/wishpage.html"


class cartpage(ListView):
    model = UserCart
    template = "cart/cartpage.html"    

class addtocart(View):
    def get(self, request, product_id):
        # This view can handle GET requests, but it doesn't perform any action for GET.
        return redirect('home-page')  # Redirect to the cart page

    def post(self, request, product_id):
        # Get the product based on the product_id
        product = get_object_or_404(Product, id=product_id)

        # Check if 'cart' is in the session, if not, create an empty list
        if 'cart' not in request.session:
            request.session['cart'] = []

        cart = request.session['cart']

        # Check if the product ID is already in the cart
        if product.id not in cart:
            # If the product ID is not in the cart, add it
            cart.append(product.id)

        # Save the updated cart back to the session
        request.session['cart'] = cart

        return redirect('home-page')  # Redirect to the cart page after adding the item