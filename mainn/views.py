from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'usuarios/home.html')

def home1(request):
    return render(request,'usuarios/home1.html')

def home2(request):
    return render(request,'usuarios/home2.html')

def home3(request):
    return render(request,'usuarios/home3.html')

def home4(request):
    return render(request,'usuarios/home4.html')
