from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .forms import CreateNewUser
from .models import *



def signup(request):
    if request.method == "POST":
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CreateNewUser()
    return render(request, "LCS/signup.html", {'form': form})


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'LCS/login.html', context)

def logoutuser(request):
    logout(request)
    return redirect('login')

def home(request):
    products = Product.objects.all()
    return render(request, 'LCS/dashboard.html', {'products': products})

def cart(request):
    return render(request, 'LCS/cart.html')

def pack(request):
    products = Product.objects.all()
    cart = Cart(request)
    cart.clear()
    return render(request, 'LCS/dashboard.html', {'products': products, 'cart': cart})



def cart_add(request, id):
    cart = Cart(request)
    products = Product.objects.all()
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return render(request, 'LCS/dashboard.html', {'products': products, 'cart': cart})

def item_clear(request, id):
    cart = Cart(request)
    products = Product.objects.all()
    product = Product.objects.get(id=id)
    cart.remove(product)
    return render(request, 'LCS/dashboard.html', {'products': products, 'cart': cart})

def item_increment(request, id):
    products = Product.objects.all()
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return render(request, 'LCS/dashboard.html', {'products': products, 'cart': cart})


def item_decrement(request, id):
    products = Product.objects.all()
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return render(request, 'LCS/dashboard.html', {'products': products, 'cart': cart})

def cart_clear(request):
    products = Product.objects.all()
    cart = Cart(request)
    cart.clear()
    return render(request, 'LCS/dashboard.html', {'products': products, 'cart': cart})

def get_total(request, id=1):
    cart = Cart(request)
    products = Product.objects.all()
    product = Product.objects.get(id=id)
