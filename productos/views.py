from django.shortcuts import render

def Index(request):
    return render(request, 'productos/index.html')