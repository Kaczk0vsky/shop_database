from django.contrib import admin
from .models import (
    Users,
    Products,
    Categories,
    Whishlist,
    WhishlistItems,
    ProductCategories,
    Shipments,
    Orders,
    Revievs,
    Adresses,
    OrderedItems,
)

admin.site.register(Users)
admin.site.register(Products)
admin.site.register(Categories)
admin.site.register(Whishlist)
admin.site.register(WhishlistItems)
admin.site.register(ProductCategories)
admin.site.register(Shipments)
admin.site.register(Orders)
admin.site.register(Revievs)
admin.site.register(Adresses)
admin.site.register(OrderedItems)
