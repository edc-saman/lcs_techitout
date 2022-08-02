from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateNewUser
from .models import *
from django.http import HttpResponse

def signup(request):
    if request.method == "POST":
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
            print("Successfully Added")
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


def base(request):
    return HttpResponse("Welcome to Logistics Control System")

