from pipes import Template
from django.http import HttpResponse
from django.shortcuts import render
from AppEntregable.models import Familia
from django.template import Context, Template
from django.template import loader

def familiar(self):
    
        familiar= Familia(nombre="Franco", edad="21", nacimiento="2001-07-03")
        familiar_dos= Familia(nombre="Maria", edad="48", nacimiento="1974-03-02")
        familiar_tres= Familia(nombre="Eduardo", edad="50", nacimiento="1971-03-20")
        familiar.save() 
        familiar_dos.save()
        familiar_tres.save()   
        texto= f"{familiar.nombre} {familiar.edad} {familiar.nacimiento}"
        texto_dos= f"{familiar_dos.nombre} {familiar_dos.edad} {familiar_dos.nacimiento}"
        texto_tres= f"{familiar_tres.nombre} {familiar_tres.edad} {familiar_tres.nacimiento}"
        return HttpResponse(texto,texto_dos, texto_tres)

def templatehtml(self):
    mihtml = open("C:/Users/Franco/Desktop/ProyectoMTV/ProyectoEntregable/Plantillas/template.html")

    plantilla = Template(mihtml.read())

    mihtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)

    




