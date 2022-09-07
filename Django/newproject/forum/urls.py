from django.urls import path

from .views import user_login, user_register,base,user_logout,account_view

urlpatterns = [
    path('',base,name= 'base'),
    path('user_login',user_login,name='user_login'),
    path('user_register',user_register,name='user_register'),
    path('user_logout',user_logout,name='user_logout'),
    path('profile',account_view, name="account" ),
]