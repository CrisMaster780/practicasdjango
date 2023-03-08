from django.urls import path, include
from . import views

urlpatterns = [
    path('productos/', views.Index, name='Productos'),
    path('productos/nuevo/', views.nuevo, name='Nuevo'),
  
]