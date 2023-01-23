from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import User, Product


def user_login(request):
    template = loader.get_template("user_login.html")
    if request.method == "POST":
        e_mail = request.POST["e_mail"]
        password = request.POST["password"]
        dict = User.objects.filter(e_mail=e_mail).values("password").get()
        if password == dict["password"]:
            return HttpResponseRedirect("/shop/shop/")
    return HttpResponse(template.render({}, request))


def shop(request):
    product_data = Product.objects.values().all()
    template = loader.get_template("shop.html")
    data = {
        "products": product_data,
    }
    if request.method == "POST":
        # adding to whishlist
        return HttpResponseRedirect("/shop/added_to_cart/")
    return HttpResponse(template.render(data, request))


def added_to_cart(request):
    product_data = Product.objects.values().all()
    template = loader.get_template("shop.html")
    data = {
        "products": product_data,
    }
    return HttpResponse(template.render(data, request))
