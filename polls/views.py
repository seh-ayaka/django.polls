from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá Mundo! Esta é a página iniciail do aplicativo.")

def sobre(request):
    return HttpResponse("Esta é a página sobre o meu site.")