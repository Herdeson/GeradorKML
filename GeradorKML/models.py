# -*- coding: utf-8 -*-
'''
Created on 19/06/2015

@author: herdeson
'''
from django.db import models

class Controle(models.Model):
    
    dataCriacao = models.DateField(auto_now_add=True,verbose_name = u"Data da Criação")
    dataModificacao = models.DateField(auto_now=True,verbose_name = u"Data da Modificação")    
    status = models.BooleanField()
    #modificador = models.ForeignKey(User)
    ip_host = models.CharField(max_length=15, blank = True, null = True)
    #nome_host = models.CharField(max_length=20, blank = True, null = True)
    
    class Meta:
        abstract = True
