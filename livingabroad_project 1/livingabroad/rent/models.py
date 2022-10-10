from django.db import models
import csv
# Create your models here.


class England_rent(models.Model):
    img = models.URLField('link')
    link = models.URLField('link')
    price = models.CharField('price',max_length=30)
    description = models.CharField('description', max_length=250)
    location = models.CharField('location', max_length=250)
    rooms_flat = models.CharField('rooms_flat', max_length=200)
    title = models.CharField('title',max_length=50)
    


class Scotland_rent(models.Model):
    img = models.URLField('link')
    link = models.URLField('link')
    price = models.CharField('price',max_length=30)
    description = models.CharField('description', max_length=150)
    location = models.CharField('location', max_length=150)
    rooms_flat = models.CharField('rooms_flat', max_length=150)
    title = models.CharField('title',max_length=50)
    
class Northireland_rent(models.Model):
    img = models.URLField('link')
    link = models.URLField('link')
    price = models.CharField('price',max_length=30)
    description = models.CharField('description', max_length=150)
    location = models.CharField('location', max_length=150)
    rooms_flat = models.CharField('rooms_flat', max_length=150)
    title = models.CharField('title',max_length=50)
    
    
class Wales_rent(models.Model):
    img = models.URLField('link')
    link = models.URLField('link')
    price = models.CharField('price',max_length=30)
    description = models.CharField('description', max_length=150)
    location = models.CharField('location', max_length=150)
    rooms_flat = models.CharField('rooms_flat', max_length=150)
    title = models.CharField('title',max_length=50)
    
    
    
    