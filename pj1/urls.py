from django.urls import path
from pj1.views import index,register,showuser
from pj1 import views

urlpatterns = [
    path('',index,name=''),
    path('/',index,name=''),
    path('index',index),
    path('register',register),
    path('showuser',showuser),
    path('adduser',views.adduser),
    path('loginto',views.loginto),
    path('login',views.login),
    path('logout',views.logout),
    path('showproduct',views.showproduct),
    path('admin_u',views.admin_u)
]
