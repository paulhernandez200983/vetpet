from django.urls import path
from . import views

app_name = 'food'
urlpatterns =[
path ('chicken', views.chicken, name=('chicken')),

]
