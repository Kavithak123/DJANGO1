
from django.contrib import admin
from django.urls import path
from SHOP import views
app_name="SHOP"
urlpatterns = [

    path('',views.allProdCat,name="allProdCat"),
    path('allproducts/<slug:cslug>',views.allproducts,name="allproducts"),
    path('prodetail/<slug:pslug>', views.prodetail, name="prodetail"),

    path('REGISTER/', views.register, name="register"),
    path('LOGIN/', views.user_login, name="user_login"),
    path('LOGOUT/', views.user_logout, name="user_logout"),


]
