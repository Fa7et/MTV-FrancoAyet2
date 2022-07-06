from pipes import Template
from django.http import HttpResponse
from django.shortcuts import render
from AppEntregable.models import Familia
from django.template import Context, Template
from django.template import loader

def familiar(self):
    
        familiar= Familia(nombre="Franco", edad="21", nacimiento="2001-07-03")
        familiar.save() 
        texto= f"{familiar.nombre} {familiar.edad} {familiar.nacimiento}"
        return HttpResponse(texto)

def familiar2(self):
        familiar= Familia(nombre="Maria", edad="48", nacimiento="1973-02-03")
        familiar.save()
        documentoDetexto= f"{familiar.nombre} {familiar.edad} {familiar.nacimiento}"
        return HttpResponse(documentoDetexto)

def familiar3(self):
        familiar= Familia(nombre="Eduardo", edad="50", nacimiento="1971-03-20")
        familiar.save()
        documentoDetexto= f"{familiar.nombre} {familiar.edad} {familiar.nacimiento}"
        return HttpResponse(documentoDetexto)



def templatehtml(self):
    mihtml = open("C:/Users/Franco/Desktop/ProyectoMTV/ProyectoEntregable/Plantillas/template.html")

    plantilla = Template(mihtml.read())

    mihtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)

    




