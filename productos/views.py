from django.shortcuts import render
from productos.models import Productos, Impuesto

def Index(request):
    _productos = Productos.objects.all()

    return render(request, 'productos/index.html' , {
        'productos':_productos
    })




def nuevo(request):
    _impuesto = Impuesto.objects.all()

    if request.method == 'GET':
        return render(request, 'productos/nuevo.html' , {
        'impuestos':_impuesto
        })
    else:
        print(request.POST)

        return render(request, 'productos/nuevo.html' , {
            'impuestos':_impuesto
        })

