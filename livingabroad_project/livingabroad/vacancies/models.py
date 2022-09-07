import csv

from django.db import models
import csv

# Create your models here.


    
class Vacancies(models.Model):
    title = models.CharField('title',max_length=50,default='no title')
    link = models.URLField('link',default='no link')
    link_company = models.URLField('link_company',default='no link')
    name_company = models.CharField('name_company', max_length=50,default='no name_company')
    salary = models.CharField('salary',max_length=30,default='not provided')
    description = models.CharField('description', max_length=250,default='no description')
    location = models.CharField('location', max_length=250,default='-')
    class Meta:
        ordering = ['-salary']

class Vacancies_scotland(models.Model):
    link = models.URLField('link',default='no link')
    title = models.CharField('title',max_length=50,default='no title')
    link_company = models.URLField('link_company',default='no link')
    name_company = models.CharField('name_company', max_length=50,default='no name_company')
    salary = models.CharField('salary',max_length=30,default='not provided')
    description = models.CharField('description', max_length=250,default='no description')
    location = models.CharField('location', max_length=250,default='-')
    class Meta:
        ordering = ['-salary']


class Vacancies_wales(models.Model):
    title = models.CharField('title',max_length=50,default='no title')
    link = models.URLField('link',default='no link')
    link_company = models.URLField('link_company',default='no link')
    name_company = models.CharField('name_company', max_length=50,default='no name_company')
    salary = models.CharField('salary',max_length=30,default='not provided')
    description = models.CharField('description', max_length=250,default='no description')
    location = models.CharField('location', max_length=250,default='-')
    class Meta:
        ordering = ['title']

class Vacancies_northireland(models.Model):
    title = models.CharField('title',max_length=50,default='no title')
    link = models.URLField('link',default='no link')
    link_company = models.URLField('link_company',default='no link')
    name_company = models.CharField('name_company', max_length=50,default='no name_company')
    salary = models.CharField('salary',max_length=30,default='not provided')
    description = models.CharField('description', max_length=250,default='no description')
    location = models.CharField('location', max_length=250,default='-')
    
    class Meta:
        ordering = ['-salary']



    def __str__(self):
        return self.title  # возвращает название объекта



    

    
    