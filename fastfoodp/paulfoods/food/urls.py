from django.urls import path
from . import views
from .views import profile
from .views import detailsv
from django.contrib.auth import views as auth_views
from .views import ver_carrito_y_pagar
from .views import  procesar_pago
from .views import  process_payment
from .views import  payment_process



app_name = 'food'
urlpatterns =[
    
path ('chicken', views.chicken, name=('chicken')),
path ('burger', views.burger, name=('burger')),
path ('drink', views.drink, name=('drink')),
path ('contact', views.contact, name=('contact')),
path ('steak', views.steak, name=('steak')),
path ('pizza', views.pizza, name=('pizza')),
path ('order', views.order, name=('order')),
path ('succes', views.succes, name=('succes')),
path ('signup', views.signup, name=('signup')),
path ('login/', views.logIn, name=('login')),
path ('logout', views.logOut, name=('logout')),
path('pizza/', profile, name='profile'),
path('details/<int:chicken_id>/', views.detailsv, name=('details')),
path('login/', auth_views.LoginView.as_view(), name='login'),
path('agregar_al_carrito/<int:chicken_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
path('eliminar_del_carrito/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
path ('ver_carrito_y_pagar/',views.ver_carrito_y_pagar, name=('ver_carrito_y_pagar')),
path('procesar-pago/', procesar_pago, name='procesar_pago'),
path('process-payment/', process_payment, name='process_payment'),
path('payment_process/', payment_process, name='payment_process'),
path('checkoutp/<int:product_id>/', views.CheckOutp, name='checkoutp'),
    path('payment-success/<int:product_id>/', views.PaymentSuccessful, name='payment-success'),
    path('payment-failed/<int:product_id>/', views.paymentFailed, name='payment-failed'),
path ('ver_carrito_y_pagarp/',views.ver_carrito_y_pagarp, name=('ver_carrito_y_pagarp')),



]
