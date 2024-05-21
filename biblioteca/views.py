#from django.shortcuts import render 
from django.http import HttpResponse

def home(request):
    print('Biblioteca')
    return HttpResponse('Página principal da Biblioteca')
