from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='photos/products')

    def __str__(self):
        return self.product_name

class Deal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    discount_percentage = models.IntegerField( default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
