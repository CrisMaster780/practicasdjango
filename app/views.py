from django.shortcuts import render

def Index(request):
    print(request.POST)
    return render(request, 'base/login.html')
