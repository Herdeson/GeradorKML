# -*- coding: utf-8 -*-
'''
Created on 20/08/2015

@author: herdeson
'''

from celery import  task
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import LocationHistory
from django.conf import settings
import csv
import os


def avisar(arquivo, email_destino):
    fdir, fname = os.path.split(arquivo)
    menssagem = 'Os dados referente ao arquivo %s foram inseridos com sucesso.' % fname.upper()
    send_mail("[AVISO] DADOS INSERIDOS", menssagem, settings.EMAIL_HOST_USER, [email_destino], fail_silently=False)

def importa_CVS(id_user, f):
    aberto = csv.reader(open(f,"rb"))
    
    for row in aberto:
        if len(row) < 9 or row[0] == 'account':
            continue
        
        print "Aki"        
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
        """
        if(novo.hora >= '07:00' and novo.hora <'12:00'):
            novo.turno = '1' #Manhã
        elif (novo.hora >= '12:00' and novo.hora < '18:00'):
            novo.turno ='2' #Tarde
        elif (novo.hora >= '18:00' and novo.hora < '00:00'):
            novo.turno = '3' #Noite
        else:
            novo.turno = '4'
        """
        novo.save()
        
    os.remove(f)
    #avisar(f, novo.modificador.email)
    

@task(ignore_result=True)
def tarefa_importar(id_user, filename):
    importa_CVS(id_user, filename)
        
    