from django.db import models
from home.models import Product
# Create your models here.
class UserCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cartid = models.IntegerField()
    
class UserWishList(models.Model):
    product = models. models.ForeignKey(Product, on_delete=models.CASCADE)
    wishid = models.IntegerField()
