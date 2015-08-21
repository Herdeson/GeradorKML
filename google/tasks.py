# -*- coding: utf-8 -*-s
'''
Created on 20/08/2015

@author: herdeson
'''

from celery import  task
from django.contrib.auth.models import User
from .models import LocationHistory
import csv


def importa_CVS(id_user, f):
    aberto = csv.reader(open(f,"rb"))
    
    for row in aberto:
        if len(row) < 9 or row[0] == 'account':
            continue
                
        novo = LocationHistory()
        novo.conta = row[0]
        novo.data = row[1]
        novo.hora = row[2]
        novo.latitude = row[3]
        novo.longitude = row[4]
        novo.raio_mapa = row[5]
        novo.origem = row[6]
        novo.device_tag = row[7]
        novo.plataforma = row[8]
        
        novo.modificador = User.objects.get(id = id_user)
        novo.status = True
        
        if(novo.hora >= '07:00' and novo.hora <'12:00'):
            novo.turno = '1' #Manhã
        elif (novo.hora >= '12:00' and novo.hora < '18:00'):
            novo.turno ='2' #Tarde
        elif (novo.hora >= '18:00' and novo.hora < '00:00'):
            novo.turno = '3' #Noite
        else:
            novo.turno = '4'
        
        novo.save()

@task(ignore_result=True)
def tarefa_importar(id_user, filename):
    importa_CVS(id_user, filename)
        
    