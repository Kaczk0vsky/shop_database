from django.urls import path

from . import views

urlpatterns = [
    path("user_login/", views.user_login, name="UserLogin"),
    path("shop/", views.shop, name="Shop"),
    path("added_to_cart/", views.added_to_cart, name="AddedToCart"),
]
