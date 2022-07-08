from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from AppEloy.models import Padre
from AppEloy.models import Madre

# Create your views here.
def padre(self):
    padre = Padre(nombre="juan",edad=64)
    padre.save()
    texto=f"Padre creado:{padre.nombre} {padre.edad} {padre.nacimiento}"
    return HttpResponse(texto)
