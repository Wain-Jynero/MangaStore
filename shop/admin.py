from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'author', 'tags',
                    'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    # Задать поля, которые могут быть отредактированы
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Product, ProductAdmin)
