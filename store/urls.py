from django.contrib import admin
from django.urls import path
from .views.home import Index , store, back_to_store
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
# from .views.otp import register, otp_form
from .middlewares.auth import  auth_middleware
from .views.search import search
from .views.tryon_glasses import try_on_glasses
from .views.quiz import quiz,get_selected_button1
from .views.signup import otp_form
from .views.favourite_item import favourite_item, favorite_items
from .views.login import forget_password_link, change_password, forget_password,verify_otp
from . import views
urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),

    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('forget_password_link', forget_password_link, name = 'forget_password_link'),
    path('forget_password', forget_password, name = "forget_password"),
    path('change_password', change_password, name = 'change_password'),
    path('otpverify', verify_otp, name="otpverify"),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('search', search, name='search'),
    path('try_on_glasses/<int:product_id>/', try_on_glasses, name='try_on_glasses'),
    path('try_on_glasses/<int:product_id>/', back_to_store, name='back_to_store'),
    path('favourite_item/<int:product_id>/', favourite_item, name='favourite_item'),
    path('favourite_items', favorite_items, name='favourite_items'),
    path('quiz', quiz, name='quiz'),
    path('male_response', get_selected_button1, name='male_response'),
    path('otp',otp_form,name="otpform")


]
