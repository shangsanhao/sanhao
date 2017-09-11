# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from models import UserInfo


# Create your views here.


def user_login(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, "user_login.html")


def user_register(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, "user_register.html")


def user_manages(request):
    user_name = request.POST.get("user_name", "")
    users = query_all(user_name=user_name)
    return render(request, "user_manages.html", {
        "users": users,
    })


def query_all(user_name):
    users = UserInfo.objects.order_by("user_name").filter(user_name=user_name)
    return users


