# myapp/models.py
from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, default="Default Title")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=100,default = "")
    image = models.ImageField(upload_to='product_images/')  # Change to your desired image field type
    image = models.URLField()
    rate = models.FloatField()
    count = models.IntegerField()

    def __str__(self):
        return self.title



class UserCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cartid = models.IntegerField()
    
    def __str__(self):
        return self.cartid
    
class UserWishList(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    wishid = models.IntegerField()

    def __str__(self):
        return self.wishid