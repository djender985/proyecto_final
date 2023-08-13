from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def bienvenida_tiles (request):
    respuesta_http= render(
        request=request,
        template_name='inicio.html',
        context={},
    )
    return respuesta_http

def acerca_de (request):
    respuesta_http= render(
        request=request,
        template_name='about.html',
        context={},
    )
    return respuesta_http