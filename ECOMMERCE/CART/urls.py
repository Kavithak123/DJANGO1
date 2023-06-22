
from django.contrib import admin
from django.urls import path
from CART import views
app_name="CART"
urlpatterns = [
    path('ADD_CART/<int:p>',views.add_cart,name="add_cart"),
    path('CART_VIEW',views.cart_view,name="cart_view"),
    path('CART_REMOVE/<int:p>', views.cart_remove, name="cart_remove"),
    path('FULL_REMOVE/<int:p>', views.full_remove, name="full_remove"),
    path('CART_VIEW', views.cart_view, name="cart_view"),
    path('ORDERFORM/', views.order, name="orderform"),
    path('ORDEVIEW/', views.orderview, name="orderview"),

]
