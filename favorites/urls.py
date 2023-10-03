from django.urls import path
from . import views


urlpatterns = [
    path('', views.favorites_detail, name='favorites_detail'),
    path('add/(<product_id>)\d+', views.favorites_add, name='favorites_add'),
    path('remove/(<product_id>)d\+', views.favorites_remove, name='favorites_remove'),
]