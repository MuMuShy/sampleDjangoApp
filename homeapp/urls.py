from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('callback',CallbackView.as_view())
]
