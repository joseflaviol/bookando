from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ver_mais', views.ver_mais, name="ver_mais"),
    path('cadastro', views.cadastro, name="cadastro"),
    path('login', views.login_function, name="login"),
    path('logout', views.logout_function, name="logout")
]
