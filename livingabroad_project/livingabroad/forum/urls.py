from django.urls import path
from .import views

 
urlpatterns = [
    path('user_login', views.user_login, name='user_login'),
    path('user_register', views.user_register, name='user_register'),
    path('home', views.forumhome, name='home'),
    path('topics', views.topics, name='topics'),
    path('topics/<int:pk>', views.questionadd.as_view(), name='exactopic'),
    path('logout', views.user_logout, name='logout'),
     
]