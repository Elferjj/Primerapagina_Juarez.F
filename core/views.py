from datetime import datetime
from django.shortcuts import render

from django.http import HttpResponse

def probandoTemplate(self):
    nombre= "Fernando"
    apellido= "Juarez"

    
    diccionario= {
        "nombre": nombre,
        "apellido": apellido,
        "dia": datetime.now().date(),

    }

