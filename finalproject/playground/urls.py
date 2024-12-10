from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('products/', views.products, name='products'),
    path('cartpage/', views.cartpage, name='cartpage'),
    path('checkout/', views.checkout, name='checkout'),
    path('logout/', views.user_logout, name='logout')
    
]