from django.contrib import admin
from django.urls import path
from myFirstProject import views

urlpatterns = [
    path('', views.index),
    path('second/', views.second_page),
    path('third/', views.third_page),
    path('fourth/', views.fourth_page),
    path('fifth/', views.fifth_page),
    path('six/', views.six_page)

]