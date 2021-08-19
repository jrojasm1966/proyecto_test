from django.db import models
import re

# Create your models here.
class ClienteManager(models.Manager):
    def validador_cliente(self, data):
        errores = {}
        if len(data['nombre']) == 0:
            errores['nombre'] = 'Ingrese nombre'
        if len(data['apellido']) == 0:
            errores['apellido'] = 'Ingrese apellido'
        if len(data['rut']) == 0:
            errores['rut'] = 'Ingrese rut'
        if len(data['dv']) == 0:
            errores['dv'] = 'Ingrese dv'

        # Expresiones regulares para validación de datos ingresados   
        EMAIL = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL.match(data['email']):
            errores['email'] = "email invalido"

        if len(data['direccion']) == 0:
            errores['direccion'] = 'Ingrese direccion'

        return errores

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)    
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    dv = models.CharField(max_length=1)
    email = models.CharField(max_length=50)    
    password = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ClienteManager()
    
