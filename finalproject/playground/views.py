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
    if request.method == "POST":
        searchInput = request.POST.get('searchInput')
        categoryInput = request.POST.get('categoryInput')
        sortInput = request.POST.get('sortInput')
        search_results = Product.objects.all()
        if searchInput:
            search_results=search_results.filter(name__contains=searchInput)
        if categoryInput:
            search_results=search_results.filter(category_id=categoryInput)
        if sortInput:
            if sortInput == "2":
                search_results=search_results.order_by('-price')
            elif sortInput == "1":
                search_results=search_results.order_by('price')
        return render(request,'products.html',{'products':search_results})
    else:
        products = Product.objects.all()
        return render(request,'products.html',{'products':products})


def cartpage(request):
    return render(request,'cartpage.html')


def checkout(request):
    return render(request,'checkout.html')

 