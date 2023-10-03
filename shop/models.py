from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render
from django.utils import timezone
from taggit.managers import TaggableManager
from django.views.generic import DetailView


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    # Продукт к одной категории, а категория содержит несколько продуктов
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=200, db_index=True)  # Название продукта
    # Алиас продукта (его URL)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(
        upload_to='products/%Y/%m/%d', blank=True, verbose_name='Изображение')   # Изображение продукта
    description = models.TextField(blank=True, verbose_name='Описание')  # Описание продукта
    author = models.TextField(blank=True, verbose_name='Автор')
    tags = TaggableManager(blank=True, verbose_name='Тэги')
    # Цена, избежать проблем округления
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    stock = models.PositiveIntegerField()
    views = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True, verbose_name='Доступен')  # Доступен продукт или нет
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')  # Дата создания объекта
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлён')  # Дата обновления объекта

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)   # Задать индекс для полей

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])