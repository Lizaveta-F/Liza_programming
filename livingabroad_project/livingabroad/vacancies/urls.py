from django.urls import path
from . import views # из этой же папки импортируем views



urlpatterns = [
    path('',views.vacancies, name = 'vacancies'),
       
]

