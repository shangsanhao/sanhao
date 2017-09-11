# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
# Create your views here.


def index(request):
    return render(request, "index.html", {
        "index_title": u"三好的博客",
    })


# 获取天气
def get_weather(request):
    if request.method == "GET":
        response = requests.get("http://api.map.baidu.com/telematics/v3/weather?location=zhengzhou&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?")
        # result是一个json字符串
        result = response.text
        return HttpResponse(result, content_type="application/json")
    return render(request, "index.html")


# 获取音乐
def get_music(request):
    if request.method == "GET":
        get_type = request.GET.get("type", "")
        if get_type:
            response = requests.get("http://tingapi.ting.baidu.com/v1/restserver/ting?method=baidu.ting.billboard.billList&format=json&type=2&offset=0&size=50")
            result = response.text
            return HttpResponse(result, content_type="application/json")
    return render(request, "music.html", {
        "music_title": u"音乐排行榜"
    })




