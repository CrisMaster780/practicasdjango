from django.shortcuts import render
from productos.models import Productos, Impuesto

def Index(request):
    _productos = Productos.objects.all()

    return render(request, 'productos/index.html' , {
        'productos':_productos
    })

def nuevo(request):
    return render(request, 'productos/nuevo.html' , {
       
    })
