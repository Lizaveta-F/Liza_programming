from django.db import models
# Create your models here.

class CommonDataAbstractModel(models.Model):
    """
        Abstract model for storing common data
    """
    title = models.CharField('title',max_length=50,default='no title')
    link = models.URLField('link',default='no link')
    link_company = models.URLField('link_company',default='no link')
    name_company = models.CharField('name_company', max_length=50,default='no name_company')
    salary = models.CharField('salary',max_length=30,default='not provided')
    description = models.CharField('description', max_length=250,default='no description')
    location = models.CharField('location', max_length=250,default='-')
    class Meta:
        abstract = True
    
class Vacancies(CommonDataAbstractModel):
    class Meta:
        ordering = ['-salary']
        verbose_name = 'Vacancy in England'
        verbose_name_plural = 'Vacancies in England'
    def __str__(self):
        return self.title  # возвращает название объекта


class Vacancies_scotland(CommonDataAbstractModel):
    class Meta:
        ordering = ['-salary']
        verbose_name = 'Vacancy in Scotland'
        verbose_name_plural = 'Vacancies in Scotland'
    def __str__(self):
        return self.title  # возвращает название объекта



class Vacancies_wales(CommonDataAbstractModel):
    class Meta:
        ordering = ['-salary']
        verbose_name = 'Vacancy in Wales'
        verbose_name_plural = 'Vacancies in Wales'
    def __str__(self):
        return self.title  # возвращает название объекта

class Vacancies_northireland(CommonDataAbstractModel):
    class Meta:
        ordering = ['-salary']
        verbose_name = 'Vacancy in Northern Ireland'
        verbose_name_plural = 'Vacancies in Northern Ireland'
    def __str__(self):
        return self.title  # возвращает название объекта



    

    
    