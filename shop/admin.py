from django.contrib import admin
from .models import (
    User,
    Product,
    Category,
    Whishlist,
    WhishlistItem,
    ProductCategory,
    Shipment,
    Order,
    Reviev,
    Adress,
    OrderedItem,
)

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Whishlist)
admin.site.register(WhishlistItem)
admin.site.register(ProductCategory)
admin.site.register(Shipment)
admin.site.register(Order)
admin.site.register(Reviev)
admin.site.register(Adress)
admin.site.register(OrderedItem)
