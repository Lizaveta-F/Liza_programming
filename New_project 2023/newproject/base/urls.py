from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create, name = 'create'),
    path('change/<int:pk>', views.edit, name = 'change'),
    path('delete/<int:pk>', views.delete, name = 'delete'),
]