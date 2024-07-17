from django.db import models
class  Product(models.Model):
    product_name = models.CharField(max_length=100, unique=True)
    price = models.IntegerField()
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='photos/products')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.product_name




