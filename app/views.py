from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from app.models import Sucursal
from django.contrib.auth.models import User


def Index(request):
    if request.method == 'GET':
        return render(request, 'base/login.html')
    else:
        _username = request.POST.get('username')
        _password = request.POST.get('password')
        user = authenticate(request, username=_username, password=_password)
        if user is None:
            return render(request, 'base/login.html', {
                'error': 'USUARIO O CONTRASENA INCORRECTOS'
            })
        else:
            login(request, user)

    return redirect(Principal)


def Principal(request):
    usuario = request.user.username
    id_usu = request.user.id
    estr = Sucursal.objects.filter(usuario__id__contains=id_usu).first()
    titulo = 'Principal'
    return render(request, 'base/index.html',  {
        'usuario': usuario,
        'titulo': titulo,
        'sucursal': estr

    })


def salir(request):
    logout(request)
    return redirect("/")
