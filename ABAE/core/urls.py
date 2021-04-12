from django.urls import path
from .views import home, registro_usuario

urlpatterns = [
    path('', home, name="home"),
    path('registro/', registro_usuario, name="registro de usuario"),

]