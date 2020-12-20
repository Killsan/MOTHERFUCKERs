from django.urls import path
from .views import *

app_name='indx'
urlpatterns = [
    path('', index, name='index'),
    path('photos/', photosView, name='photos'),
    path('test/', testView, name='test'),
    path('test/questions/', questionsView, name='questions'),
    path('test/questions/result/', resultView, name='result'),
]