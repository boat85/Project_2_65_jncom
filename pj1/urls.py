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
    path('admin_u',views.admin_u),
    path('add_product',views.add_product),
    path('add_prod',views.add_prod),
    path('showallproducts',views.showallproducts),
    path('delete_product',views.delete_product),
    path('showallusers',views.showallusers),
    path('showwhileproducts',views.showwhileproducts),
    path('swhileproducts',views.swhileproducts)
    
    
    
]
