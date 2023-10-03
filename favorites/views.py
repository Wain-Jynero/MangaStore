from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .favorites import Favorites
from cart.forms import CartAddProductForm
from django.http import HttpResponseRedirect, HttpResponse

@require_POST
def favorites_add(request, product_id):
    favorites = Favorites(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        favorites.add(product=product)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def favorites_remove(request, product_id):
    favorites = Favorites(request)
    product = get_object_or_404(Product, id=product_id)
    favorites.remove(product)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def favorites_detail(request):
    favorites = Favorites(request)
    return render(request, 'favorites/favorites.html', {'favorites': favorites})