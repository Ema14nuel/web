from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductoView

url_principal = 'producto/'

urlpatterns = [
    path('', ProductoView.Inicio.as_view(), name='inicio'),
    path('nosotros/', ProductoView.Nosotros.as_view(), name='nosotros'),
    path('producto/', ProductoView.ProductoListaView.as_view(), name='producto'),
]

