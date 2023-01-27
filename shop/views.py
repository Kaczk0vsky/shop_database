from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import User, Product, Whishlist, WhishlistItem
from .global_vars import user_dict


def user_login(request):
    template = loader.get_template("user_login.html")
    if request.method == "POST":
        # getting data from html template
        e_mail = request.POST["e_mail"]
        password = request.POST["password"]
        dict = User.objects.filter(e_mail=e_mail).values("password").get()
        # checking if user existing in database is correct with the given one
        if password == dict["password"]:
            user_dict["password"] = password
            user_dict["e_mail"] = e_mail
            return HttpResponseRedirect("/shop/shop/")
    return HttpResponse(template.render({}, request))


def shop(request):
    # loading products database into html template
    product_data = Product.objects.raw("SELECT * FROM shop_product")
    template = loader.get_template("shop.html")
    data = {
        "products": product_data,
    }
    # action after clicking the button on site
    if request.method == "POST":
        # getting quantity of items bought
        amount = request.POST.getlist("amount")
        quantity = [eval(x) for x in amount]
        # checking if wishlist for logged user was previously created
        if Whishlist.objects.filter(
            user_id=User.objects.get(e_mail=user_dict["e_mail"])
        ).exists():
            pass
        else:
            Whishlist(
                user_id=User.objects.get(e_mail=user_dict["e_mail"]),
                name=f"User {user_dict['e_mail']} whishlist",
            ).save()
        # adding items to WhishlistItems
        i = 1
        for x in quantity:
            while x > 0:
                WhishlistItem(
                    whishlist_id=Whishlist.objects.get(
                        name=f"User {user_dict['e_mail']} whishlist"
                    ),
                    product_id=Product.objects.get(id=i),
                ).save()
                x = x - 1
            i = i + 1
        # removing added products from shop
        quantity = [eval(x) for x in amount]
        i = 1
        for x in quantity:
            obj = Product.objects.get(id=i)
            product_amount = obj.quantity
            product_amount = product_amount - x
            Product.objects.filter(id=i).update(quantity=product_amount)
            i = i + 1
        return HttpResponseRedirect("/shop/added_to_cart/")
    return HttpResponse(template.render(data, request))


def added_to_cart(request):
    products = Product.objects.values("name", "price").all()
    template = loader.get_template("added_to_cart.html")
    # counting how many items are on whishlist
    i = Product.objects.count()
    index = 1
    product_data = []
    while index <= i:
        data = (
            WhishlistItem.objects.filter(
                whishlist_id=Whishlist.objects.get(
                    user_id=User.objects.get(e_mail=user_dict["e_mail"])
                ),
                product_id=index,
            )
        ).count()
        product_data.append(data)
        index = index + 1
    # addind items to dict
    data = {
        "name": products,
        "products": product_data,  # quantity,
    }
    print(data)
    # adding back to shop button action
    if request.method == "POST":
        return HttpResponseRedirect("/shop/shop/")
    return HttpResponse(template.render(data, request))
