from email.policy import default
from django.db import models

# Create your models here.

class Product(models.Model):
    
    def __str__(self):
        return self.title
    
    title = models.CharField(max_length = 200)
    price = models.FloatField()
    discount_price = models.FloatField()
    caregory = models.CharField(max_length = 200)
    description = models.TextField()
    image = models.CharField(max_length = 400)
    
    
class Order(models.Model):
    
    def __str__(self):
        return self.name
    
    items = models.CharField(max_length = 1000)
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 200)
    adress = models.CharField (max_length = 300)
    city = models.CharField (max_length = 200)
    state = models.CharField (max_length = 200)
    zip = models.CharField (max_length = 200)
    total = models.FloatField (default=1)