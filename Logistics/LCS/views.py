from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .forms import CreateNewUser, CustomerForm
from .models import *


def signup(request):
    success_message = ''
    if request.method == "POST":
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
            success_message = "User Created Successfully!"
            return redirect('login')
    else:
        form = CreateNewUser()
    return render(request, "LCS/signup.html", {'form': form, 'success_message': success_message})


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
    customer = customer_data(request)
    return render(request, 'LCS/dashboard.html', {'products': products, 'customer': customer})

def cart(request):
  template = get_template('LCS/cart.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
      success_message =''
      x = request.POST['first']
      y = request.POST['last']
      a = request.POST['mobile']
      b = request.POST['email']
      c = request.POST['address']
      member = Customer(first_name=x, last_name=y, mobile=a, email_address=b,address=c)
      member.save()
      #return HttpResponseRedirect(reverse('cart'))
      return render(request, 'LCS/cart.html')

def cart1(request,id):
    item = get_object_or_404(Product,id=id)
    order_item, created = Order_Item.objects.get_or_create(item=item,user=request.user,ordered=False)
    order_filter = Order.objects.filter(user=request.user, ordered=False)
    if order_filter.exists():
        order = order_filter[0]
        if order.items.filters(id=id).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        ordered_date = timezone.now
        order = Order.objects.create(user=request.user,ordered_date=ordered_date)
        order.items(order_item)

    return redirect("LCS/cart.html",id=id)


def customer_data(request):
    if request.method == "POST":
        customer = CustomerForm(request.POST)
        if customer.is_valid():
            customer.save()
    else:
        customer = CustomerForm()

    return customer


def pack(request):
    products = Product.objects.all()
    customer = customer_data(request)
    cart = Cart(request)
    cart.clear()
    return render(request, 'LCS/dashboard.html', {'products': products, 'cart': cart, 'customer': customer})


def cart_add(request, id):
    cart = Cart(request)
    customer = customer_data(request)
    products = Product.objects.all()
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return render(request, 'LCS/dashboard.html', {'products': products, 'cart': cart, 'customer': customer})


def item_clear(request, id):
    cart = Cart(request)
    customer = customer_data(request)
    products = Product.objects.all()
    product = Product.objects.get(id=id)
    cart.remove(product)
    return render(request, 'LCS/dashboard.html', {'products': products, 'cart': cart, 'customer': customer})


def item_increment(request, id):
    products = Product.objects.all()
    cart = Cart(request)
    customer = customer_data(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return render(request, 'LCS/dashboard.html', {'products': products, 'cart': cart, 'customer': customer})


def item_decrement(request, id):
    products = Product.objects.all()
    cart = Cart(request)
    customer = customer_data(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return render(request, 'LCS/dashboard.html', {'products': products, 'cart': cart, 'customer': customer})


def cart_clear(request):
    products = Product.objects.all()
    cart = Cart(request)
    customer = customer_data(request)
    cart.clear()
    return render(request, 'LCS/dashboard.html', {'products': products, 'cart': cart, 'customer': customer})


def get_total(request, id=1):
    cart = Cart(request)
    products = Product.objects.all()
    product = Product.objects.get(id=id)
