# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views import generic
from django.template.context_processors import csrf
import csv
import os
from .forms import UploadCvs, FiltroForm
from .models import LocationHistory
from GeradorKML.settings import MEDIA_ROOT
from datetime import date


# Create your views here.


def importa_CVS(f):
    aberto = csv.reader(open(f,"rb"))
    
    for row in aberto:
        if len(row) < 9 or row[0] == 'account':
            continue
                
        novo = LocationHistory()
        novo.conta = row[0]
        #novo.data = datetime.strptime(row[1], '%Y-%m-%d').date()
        novo.data = row[1]
        novo.hora = row[2]
        novo.latitude = row[3]
        novo.longitude = row[4]
        novo.raio_mapa = row[5]
        novo.origem = row[6]
        novo.device_tag = row[7]
        novo.plataforma = row[8]
        
        novo.status = True
        
        novo.save()
        
        
    

def branco(request):
    return render_to_response('google/blank.html')

def upload_CVS(request):
    """
    LEMBRAR DE REALIZAR ALTERAÇÕES... ESTÁ SENDO FEITIO UTILIZANDNO O CAMINHO FELIZ
    É PRECISO REALIZAR O TRATAMENTO DE ARQUIVO.
    EX: NÃO FOR POSSÍVEL ELE IMPORTAR O ARQUIVO CSV
    """
    c= {}
    c.update(csrf(request))
    
    if  request.POST:
        
        form = UploadCvs(request.POST, request.FILES)
        if form.is_valid():
            #Utilizado para salvar o arquivo
            arquivo = os.path.join(MEDIA_ROOT,request.FILES['arquivo'].name)
            with open(arquivo, 'wb+') as destination:
                for chunk in request.FILES['arquivo'].chunks():
                    destination.write(chunk)
            
            #Fazer alguma coisa com o arquivo salva ou processa ele
            #No caso processa para inserir no banco de dados
            #print type(request.FILES['arquivo'])
            importa_CVS(arquivo)
            #Deletar o arquivo que foi realizado Upload
            os.remove(arquivo)
            
            hj = date.today()
            lista = LocationHistory.objects.filter(dataCriacao = hj)
            form = FiltroForm()
            c.update({'lista':lista,'form':form })
            return render_to_response('google/lista.html', c )
            
    
    form = UploadCvs()
    c.update({'form':form })
    return render(request, 'google/uploadCvs.html', c )

def listarDados(request):
    """
    Lembrar de fazer as alterações para buscar objetos relacionados a pessoa
    """
    c= {}
    c.update(csrf(request))
    
    if request.POST:
        form = FiltroForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('branco')
    
    
    form = FiltroForm()
    lista = LocationHistory.objects.order_by('-dataCriacao')
    c.update({'lista':lista})
    
    return render(request, 'google/lista.html', {'form':form, 'lista':lista})

class ListarDados(generic.ListView):
    template_name='google/lista.html'
    context_object_name = 'lista'
    
    def get_queryset(self):
        return LocationHistory.objects.order_by('-dataCriacao')
    