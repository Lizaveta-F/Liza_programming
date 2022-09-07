import csv
from django.db import models
import csv

# Create your models here.




class Vacancies(models.Model):  # создаём таблицу базы данных
    title = models.CharField('Title',max_length=50)
    salary = models.CharField('Salary',max_length=20)
    description = models.TextField('Description')
    remote = models.CharField('Remote',max_length=20)
    link = models.URLField('Link')
    city = models.CharField('City',max_length=50)
    
    # def __str__(self):
    #     return self.title  # возвращает название объекта
    
# # with open("data.csv", newline = '') as csvfile:
# #     reader = csv.reader(csvfile)
# #     for row in reader:
# #          _, created = Vacancies.objects.get_or_create(
# #                 title=row[0],
# #                 salary=row[1],
# #                 description=row[2],)
                
       
    
    