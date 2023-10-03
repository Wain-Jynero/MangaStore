from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('refund/', views.refund, name='refund'),
    path('contacts/', views.contacts, name='contacts'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('coupons/', views.coupons, name='coupons'),
    path('confidentiality/', views.confidentiality, name='confidentiality'),
    path('offer/', views.offer, name='offer'),
    path('payment/', views.payment, name='payment'),
    path('catalog/', views.product_list, name='product_list'),
    path('search/', views.search_products, name='search_products'),
    path('<category_slug>[-\w]+/',
         views.product_list,
         name='product_list_by_category'),
    path('<id>\d+)/(<slug>[-\w]+/',
         views.product_detail,
         name='product_detail'),
    path('tag/(<tag_slug>[-\w]+)/', views.product_list, name='product_list_by_tag'),
]
