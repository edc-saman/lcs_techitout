from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logoutuser, name="logout"),
    path('login', views.loginPage, name="login"),
    path('signup/', views.signup, name="signup"),
    path('dashboard/', views.home, name="home"),
    path('dashboard/add/<int:id>', views.cart_add, name='cart_add'),
    path('dashboard/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('dashboard/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('dashboard/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('dashboard/cart_clear/', views.get_total, name='get_total'),
    path('dashboard/cart-detail/',views.cart_detail,name='cart_detail'),
]
