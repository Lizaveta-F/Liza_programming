from django.urls import path
from . import views





urlpatterns = [

    path('england_rent', views.england_rent, name = 'england_rent'),
    path('scotland_rent', views.scotland_rent, name = 'scotland_rent'),
    path('wales_rent', views.wales_rent, name = 'wales_rent'),
    path('northireland_rent', views.northireland_rent, name = 'northireland_rent'),
    
       
]
