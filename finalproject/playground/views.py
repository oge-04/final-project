from django.shortcuts import render,redirect
from .models import Product
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def user_login(request):
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect(request,'login.html')

def products(request):
    products = Product.objects.all()
    if request.method == "POST":
        searchInput = request.POST.get('search')
        categoryInput = request.POST.get('categoryInput')
        sortInput = request.POST.get('sortInput')
        
        if searchInput:
            products = Product.objects.filter(name__contains=searchInput)
        if categoryInput:
            products = Product.objects.filter(category=categoryInput)
        if sortInput:
            products = Product.objects.filter(sortInput)
     


    return render(request,'products.html', {'products':products})


def cartpage(request):
    return render(request,'cartpage.html')


def checkout(request):
    return render(request,'checkout.html')

 