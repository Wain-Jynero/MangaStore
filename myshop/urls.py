"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from shop.views import index, refund, payment, contacts, aboutus, coupons, confidentiality, offer, search_products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('refund/', refund, name='refund'),
    path('payment/', payment, name='payment'),
    path('contacts/', contacts, name='contacts'),
    path('aboutus/', aboutus, name='aboutus'),
    path('coupons/', coupons, name='coupons'),
    path('offer/', offer, name='offer'),
    path('search/', search_products, name='search_products'),
    path('confidentiality/', confidentiality, name='confidentiality'),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('favorites/', include(('favorites.urls', 'favorites'), namespace='favorites')),
    path('shop/', include(('shop.urls', 'shop'), namespace='shop')),
    path('orders/', include(('orders.urls', 'orders'), namespace='orders')),
    path('coupons/', include(('coupons.urls', 'coupons'), namespace='coupons')),
    path('', include(('account.urls', 'account'), namespace='account')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
