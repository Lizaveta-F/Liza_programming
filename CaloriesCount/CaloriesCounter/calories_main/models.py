from tkinter import CASCADE
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Food(models.Model):
    
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length = 100)
    carbs = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()
    
class Consume(models.Model):
    
    def __str__(self) :
        return self.user.username
    
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    food_consumed = models.ForeignKey(Food,on_delete = models.CASCADE)
    
