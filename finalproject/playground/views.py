from django.shortcuts import render,redirect
from .models import Product, Cart
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
        cartItems = Cart.objects.all()
        totalItems = sum(item.quantity for item in cartItems)
        return render(request,'products.html',{'products':search_results, 'total_items': totalItems})
    else:
        products = Product.objects.all()
        cartItems = Cart.objects.all()
        totalItems = sum(item.quantity for item in cartItems)
        return render(request,'products.html',{'products':products, 'total_items': totalItems})


def cartpage(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity',0)
        action = request.POST.get('action')

        product = Product.objects.get(id=product_id)
        if action == 'add':
            cart, created  = Cart.objects.get_or_create(product=product, defaults={'quantity':quantity})

            if not created:
                cart.quantity += int(quantity)
                cart.save()
        elif action == 'delete':
            Cart.objects.filter(product=product).delete()
            
        
        cartItems = Cart.objects.all()
        totalItems = sum(item.quantity for item in cartItems)
        cartTotal = sum(item.totalPrice() for item in cartItems)
        return render(request, 'cartpage.html', {'cartItems': cartItems, 'total_items': totalItems, 'cartTotal': cartTotal})
    else:
        cartItems = Cart.objects.all()
        totalItems = sum(item.quantity for item in cartItems)
        cartTotal = sum(item.totalPrice() for item in cartItems)
        return render(request, 'cartpage.html', {'cartItems': cartItems, 'total_items': totalItems, 'cartTotal': cartTotal})
        


def checkout(request):
    return render(request,'checkout.html')

 