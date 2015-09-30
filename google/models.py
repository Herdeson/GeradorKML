# -*- coding: utf-8 -*-
from django.db import models
from GeradorKML.models import Controle
from .forms import TURNO
# Create your models here.


class LocationHistory(Controle):
    conta = models.CharField(max_length=50)
    data = models.DateField()
    hora = models.TimeField(null=True,blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    raio_mapa = models.IntegerField(null=True,blank=True)
    origem = models.CharField(max_length=10)
    device_tag = models.IntegerField(null=True,blank=True)
    plataforma = models.CharField(max_length=150, null=True,blank=True)
    turno = models.CharField(blank=True, null=True, max_length= 1, choices=TURNO)
    
    
    def __str__(self):
        return self.conta
    

class ArqGerados(Controle):
    arquivo = models.FilePathField()

