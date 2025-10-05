from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Product

# Homepage view
@login_required(login_url='login')
def home(request):
    return render(request, 'ecommerce/home.html')

# Product listing view
@login_required(login_url='login')
def product_list(request):
    products = Product.objects.all()
    return render(request, 'ecommerce/product_list.html', {'products': products})

# User registration view
def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password=password)
            user.email = email
            user.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'ecommerce/register.html', {'error': 'Username already exists.'})
    return render(request, 'ecommerce/register.html')

# User login view
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'ecommerce/login.html', {'error': 'Invalid credentials'})
    return render(request, 'ecommerce/login.html')

# User logout view
def logout_user(request):
    logout(request)
    return redirect('login')
