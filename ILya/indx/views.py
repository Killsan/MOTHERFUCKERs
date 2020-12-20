from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def index(request):
    return redirect('indx:main')

def main(request):
    return render(request, 'indx/main.html')

def bio(request):
    return render(request, 'indx/bio.html')

def galary(request):

    return render(request, 'indx/galary.html')

