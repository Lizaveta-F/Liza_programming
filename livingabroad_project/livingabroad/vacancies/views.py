from smtplib import SMTPResponseException
from django.shortcuts import render
# from .models import Vacancies
# from django.views.generic import DetailsView  # класс, который позволяет отслеживать динамические страницы
import csv,io

from .models import Vacancies


# Create your views here.

def vacancies(request):    
    return render(request,'vacancies/vacancies.html')

