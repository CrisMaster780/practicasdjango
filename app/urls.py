from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Index, name='Index'),
    path('principal/', views.Principal, name='Principal'),
    
]+ static(settings.STATIC_URL)
