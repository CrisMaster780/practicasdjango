from django.shortcuts import render, redirect


def Index(request):
    if request.method == 'GET':
        return render(request, 'base/login.html')
    else:
        _username = request.POST.get('username')
        _password = request.POST.get('password')

        if _username is None or _password is None:
            print('entro aca')
            error = 'Ingrese todos los datos'

            return render(request, 'base/login.html', {
                'error': error
            })
        else:


            return redirect(Principal)


def Principal(request):
    return render(request, 'base/index.html', {
               
            })


   
