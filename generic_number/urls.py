from django.contrib import admin
from django.urls import path, include
from .views import random_number, home_page, toss_a_coin, random_list, dice,generic_password
urlpatterns = [

    path('', home_page, name="home"),
    path('random_number/', random_number, name = "random" ),
    path('toss_a_coin/', toss_a_coin, name = "toss_a_coin" ),
    path('random_list/', random_list, name = "random_list" ),
    path('random_dice/', dice, name='random_dice'),
    path('generic_password/', generic_password, name='generic_password'),
]
