# -*- coding: utf-8 -*-
from django.db import models
from GeradorKML.models import Controle
# Create your models here.


class LocationHistory(Controle):
    conta = models.CharField(max_length=50)
    data = models.DateField()
    hora = models.TimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    raio_mapa = models.IntegerField()
    origem = models.CharField(max_length=10)
    device_tag = models.IntegerField()
    plataforma = models.CharField(max_length=150)
    turno = models.CharField(blank=True, null=True, max_length= 2)
    
    
    def __str__(self):
        return self.conta
    


