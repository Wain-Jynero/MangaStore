import random
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.conf import settings
from django.views.generic import ListView
from .models import Category, Product
from random import sample
from cart.forms import CartAddProductForm
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import NewUserForm, LoginForm
from django.contrib.auth import login, authenticate
from django.contrib import messages


def index(request):
    if request.method == "POST":
        reg_form = NewUserForm(request.POST)
        if reg_form.is_valid():
            user = reg_form.save()
            login(request, user)
            return redirect("index")
        messages.error(request, "Не верно введёные данные")

    if request.method == 'POST':
        log_form = LoginForm(request.POST)
        if log_form.is_valid():
            cd = log_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
    else:
        log_form = LoginForm()

    log_form = LoginForm()
    reg_form = NewUserForm()
    random_products = get_random_products()
    last_products = get_last_products()
    context = {'random_products': random_products,
               'last_products': last_products,
               "register_form":reg_form,
               'login_form': log_form}
    return render(request, 'index.html', context)

def refund(request):
    if request.method == "POST":
        reg_form = NewUserForm(request.POST)
        if reg_form.is_valid():
            user = reg_form.save()
            login(request, user)
            return redirect("index")
        messages.error(request, "Не верно введёные данные")

    if request.method == 'POST':
        log_form = LoginForm(request.POST)
        if log_form.is_valid():
            cd = log_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
    else:
        log_form = LoginForm()

    log_form = LoginForm()
    reg_form = NewUserForm()
    context = {"register_form":reg_form,
               "login_form": log_form}
    return render(request, 'refund.html', context)


def payment(request):
    if request.method == "POST":
        reg_form = NewUserForm(request.POST)
        if reg_form.is_valid():
            user = reg_form.save()
            login(request, user)
            return redirect("index")
        messages.error(request, "Не верно введёные данные")

    if request.method == 'POST':
        log_form = LoginForm(request.POST)
        if log_form.is_valid():
            cd = log_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
    else:
        log_form = LoginForm()

    log_form = LoginForm()
    reg_form = NewUserForm()
    context = {"register_form":reg_form,
               "login_form": log_form}
    return render(request, 'payment.html', context)


def contacts(request):
    if request.method == "POST":
        reg_form = NewUserForm(request.POST)
        if reg_form.is_valid():
            user = reg_form.save()
            login(request, user)
            return redirect("index")
        messages.error(request, "Не верно введёные данные")

    if request.method == 'POST':
        log_form = LoginForm(request.POST)
        if log_form.is_valid():
            cd = log_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
    else:
        log_form = LoginForm()

    log_form = LoginForm()
    reg_form = NewUserForm()
    context = {"register_form":reg_form,
               "login_form": log_form}
    return render(request, 'contacts.html', context)


def aboutus(request):
    if request.method == "POST":
        reg_form = NewUserForm(request.POST)
        if reg_form.is_valid():
            user = reg_form.save()
            login(request, user)
            return redirect("index")
        messages.error(request, "Не верно введёные данные")

    if request.method == 'POST':
        log_form = LoginForm(request.POST)
        if log_form.is_valid():
            cd = log_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
    else:
        log_form = LoginForm()

    log_form = LoginForm()
    reg_form = NewUserForm()
    context = {"register_form":reg_form,
               "login_form": log_form}
    return render(request, 'aboutUs.html', context)

def coupons(request):
    if request.method == "POST":
        reg_form = NewUserForm(request.POST)
        if reg_form.is_valid():
            user = reg_form.save()
            login(request, user)
            return redirect("index")
        messages.error(request, "Не верно введёные данные")

    if request.method == 'POST':
        log_form = LoginForm(request.POST)
        if log_form.is_valid():
            cd = log_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
    else:
        log_form = LoginForm()

    log_form = LoginForm()
    reg_form = NewUserForm()
    context = {"register_form":reg_form,
               "login_form": log_form}
    return render(request, 'coupons.html', context)


def confidentiality(request):
    if request.method == "POST":
        reg_form = NewUserForm(request.POST)
        if reg_form.is_valid():
            user = reg_form.save()
            login(request, user)
            return redirect("index")
        messages.error(request, "Не верно введёные данные")

    if request.method == 'POST':
        log_form = LoginForm(request.POST)
        if log_form.is_valid():
            cd = log_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
    else:
        log_form = LoginForm()

    log_form = LoginForm()
    reg_form = NewUserForm()
    context = {"register_form":reg_form,
               "login_form": log_form}
    return render(request, 'confid.html', context)


def offer(request):
    if request.method == "POST":
        reg_form = NewUserForm(request.POST)
        if reg_form.is_valid():
            user = reg_form.save()
            login(request, user)
            return redirect("index")
        messages.error(request, "Не верно введёные данные")

    if request.method == 'POST':
        log_form = LoginForm(request.POST)
        if log_form.is_valid():
            cd = log_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
    else:
        log_form = LoginForm()

    log_form = LoginForm()
    reg_form = NewUserForm()
    context = {"register_form":reg_form,
               "login_form": log_form}
    return render(request, 'oferta.html', context)


def product_list(request, category_slug=None, tag_slug=None):
    category = None
    categories = Category.objects.all()
    # Сортировка только доступных продуктов
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags_in=[tag])
    return render(request,
                  'list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products
                   })

def get_random_products():
    products = Product.objects.all()
    return random.sample(list(products), 5)

def get_last_products():
    return Product.objects.order_by('-id')[:6]

def search_products(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name=query)
    else:
        products = Product.objects.all()
    return render(request, 'searchprod.html', {'products': products, 'query': query})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    suggested_products = random.sample(list(Product.objects.exclude(id=id)), 3)
    cart_product_form = CartAddProductForm()
    return render(request, 'detail.html', {'product': product,
                                           'cart_product_form': cart_product_form,
                                           'suggested_products': suggested_products})