from django.shortcuts import render
from productos.models import Productos

def Index(request):
    _productos = Productos.objects.all()

    return render(request, 'productos/index.html')