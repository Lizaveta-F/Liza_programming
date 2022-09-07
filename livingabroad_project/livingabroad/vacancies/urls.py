from django.urls import path
from . import views # из этой же папки импортируем views





urlpatterns = [
    
    
    path('England/work_england',views.work_england, name = 'work_england'),
    path('Scotland/work_scotland',views.work_scotland, name = 'work_scotland'),
    path('Wales/work_wales',views.work_wales, name = 'work_wales'),
    path('Norireland/work_northireland',views.work_northireland, name = 'work_northireland'),
]
