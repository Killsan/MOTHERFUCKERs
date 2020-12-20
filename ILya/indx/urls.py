from django.urls import path 
from .views import *

app_name='indx'
urlpatterns = [
    path('', index),
    path('main/', main, name='main'),
    path('bio/', bio, name='bio'),
    path('galary/', galary, name='galary'),
]