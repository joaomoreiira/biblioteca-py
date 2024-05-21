from django.http import HttpResponse
from biblioteca import views



def home(request):
    print('Biblioteca')
    return HttpResponse('Página principal da Biblioteca')

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
]
