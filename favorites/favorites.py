from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Favorites(object):
    def __init__(self, request):
        self.session = request.session
        favorites = self.session.get(settings.FAVORITES_SESSION_ID)
        if not favorites:
            favorites = self.session[settings.FAVORITES_SESSION_ID] = {}
        self.favorites = favorites
    
    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.favorites:
            self.favorites[product_id] = {'price': str(product.price)}
        self.save()
    
    def save(self):
        self.session[settings.FAVORITES_SESSION_ID] = self.favorites
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.favorites:
            del self.favorites[product_id]
        self.save()

    def __iter__ (self):
        product_ids = self.favorites.keys()
        products = Product.objects.filter(id__in = product_ids)
        for product in products:
            self.favorites[str(product.id)]['product'] = product

        for item in self.favorites.values():
            item['price'] = Decimal(item['price'])
            yield item

    def clear(self):
        del self.session[settings.FAVORITES_SESSION_ID]
        self.session.modified = True