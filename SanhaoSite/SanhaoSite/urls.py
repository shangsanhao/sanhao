"""SanhaoSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from users import views as users_views
from main import views as main_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^index/', main_views.index),
    url(r'^user_login/', users_views.user_login, name="user_login"),
    url(r'^user_register/', users_views.user_register, name="user_register"),
    url(r'user_manages/', users_views.user_manages, name="user_manages"),
    url(r'get_weather/', main_views.get_weather, name="get_weather"),
    url(r'get_music/', main_views.get_music, name="get_music"),



    url(r'', main_views.index),


]
