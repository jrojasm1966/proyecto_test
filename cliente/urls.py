from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('inicio', views.inicio),
    path('agregar', views.agregar), # Create
    path('leer', views.leer), # Read
    path('actualizar', views.actualizar), # Update
    path('eliminar', views.eliminar), # Delete
    ]
