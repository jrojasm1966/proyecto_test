# Create your views here.
from django.shortcuts import render

from .models import Cliente

def inicio(request):
    #return HttpResponse("this is the equivalent of @app.route('/')!")
    return render(request, 'inicio.html')

def agregar(request):
    # request.post['parametro']
    # capturando los parametros enviados por el formulario
    Cliente.objects.create(
    nombre = request.POST['nombre'],
    apellido = request.POST['apellido'],
    rut = request.POST['rut'],
    dv = request.POST['dv'],
    email = request.POST['email'],
    password = request.POST['password'],
    direccion = request.POST['direccion']
    )
    return render(request, 'inicio.html')

def leer(request):
    return

def actualizar(request):
    return

def eliminar(request):
    return



