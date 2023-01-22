from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Users
from .forms import NewUser


def user_login(request):
    if request.method == "POST":
        e_mail = request.POST["e_mail"]
        password = request.POST["password"]
        dict = Users.objects.filter(e_mail=e_mail).values("password").get()
        if password == dict["password"]:
            return HttpResponseRedirect("/shop/shop/")
        else:
            return render(request, "user_login.html")


def shop(request):
    return HttpResponse("Hello, world.")
