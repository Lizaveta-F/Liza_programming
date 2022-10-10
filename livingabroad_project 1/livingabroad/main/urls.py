from django.urls import path
from . import views # из этой же папки импортируем views



urlpatterns = [
    path('',views.home,name = 'home'),
    path('GB',views.exploreGB,name = 'GB'),
    path('England',views.england,name = 'England'),
    path('Scotland',views.scotland, name = 'Scotland'),
    path('Wales',views.wales, name = 'Wales'),
    path('NorthernIreland',views.northernireland, name = "NorthernIreland"),
    path('Shopping',views.shopping, name = 'Shopping'),
    path('England/study', views.studyinengland, name = 'England/study'),
    path('Scotland/study', views.studyinscotland, name = 'Scotland/study'),
    path('Wales/study', views.studyinwales, name = 'Wales/study'),
    path('NorthernIreland/study', views.studyinnorireland, name = 'NorthernIreland/study')
       
]
