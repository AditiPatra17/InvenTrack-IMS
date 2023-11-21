from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
)

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)

    def __str__(self):
        return f'{self.name}-{self.quantity}'
    
    class Meta:
        verbose_name_plural = 'Product'
    
class Order(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return f'{self.name} ordered by {self.staff}'
    
    class Meta:
        verbose_name_plural = 'Order'