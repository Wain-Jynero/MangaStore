from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/(<product_id>\d+)', views.cart_add, name='cart_add'),
    path('remove/(<product_id>\d+)', views.cart_remove, name='cart_remove'),
]