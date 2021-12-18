from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ver_mais', views.ver_mais, name="ver_mais")
]
