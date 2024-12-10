from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def user_login(request):
    return render(request,'login.html')

def user_logout(request):
    return render(request,'logout.html')

def products(request):
    products = Product.objects.all()
    if request.method == "POST":
        search = request.POST['search']


    return render(request,'products.html', {'products':products})


def cartpage(request):
    return render(request,'cartpage.html')


def checkout(request):
    return render(request,'checkout.html')

 