# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views import generic
from django.template.context_processors import csrf, request
import csv
import os
from .forms import UploadCvs, FiltroForm
from .models import LocationHistory
from GeradorKML.settings import MEDIA_ROOT
from datetime import date , datetime
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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
        
        if(novo.hora >= '07:00' and novo.hora <'12:00'):
            novo.turno = '1' #Manhã
        elif (novo.hora >= '12:00' and novo.hora < '18:00'):
            novo.turno ='2' #Tarde
        elif (novo.hora >= '18:00' and novo.hora < '00:00'):
            novo.turno = '3' #Noite
        else:
            novo.turno = '4'
            
        
        
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
            
            #hj = date.today()
            #lista = LocationHistory.objects.filter(dataCriacao = hj)
            #form = FiltroForm()
            #c.update({'lista':lista,'form':form })
            return HttpResponseRedirect('listarGoogle')
            #return render_to_response('google/lista.html', c )
            
    
    form = UploadCvs()
    c.update({'form':form })
    return render(request, 'google/uploadCvs.html', c )

def listarDados(request):
    """
    Lembrar de fazer as alterações para buscar objetos relacionados a pessoa
    """
    c= {}
    lista = None
    c.update(csrf(request))
    form = FiltroForm(request.POST or None)
    
    if request.POST:
        if form.is_valid():
            request.session['consulta'] = True
            if 'conta' in form.changed_data:
                lista = LocationHistory.objects.filter(conta__icontains = form.data['conta'])
                request.session['conta'] = form.data['conta']
            if 'periodo' in form.changed_data:
                request.session['periodo'] = form.data['periodo']
                if lista is None:
                    lista = LocationHistory.objects.filter(turno = form.data['periodo'])
                else:
                    lista = lista.filter(turno = form.data['periodo'])
            if 'wifi' in form.changed_data and 'cell' not in form.changed_data:
                request.session['wifi'] = 'WIFI'
                if lista is None:
                    lista = LocationHistory.objects.filter(origem='WIFI')
                else:
                    lista = lista.filter(origem='WIFI')
            elif 'wifi' not in form.changed_data and 'cell' in form.changed_data:
                request.session['cell'] = 'CELL'
                if lista is None:
                    lista = LocationHistory.objects.filter(origem='CELL')
                else:
                    lista = lista.filter(origem='CELL')
            if 'dtInicio' in form.changed_data and 'dtFim' in form.changed_data:
                inicio = datetime.strptime(form.data['dtInicio'], '%d/%m/%Y').date()
                fim = datetime.strptime(form.data['dtFim'], '%d/%m/%Y').date()
                if lista is None:
                    lista = LocationHistory.objects.filter(data__range=(inicio, fim))
                else:
                    lista = lista.filter(data__range=(inicio, fim))
                
                request.session['dtInicio'] = form.data['dtInicio']
                request.session['dtFim'] = form.data['dtFim']

            
                       
            paginator = Paginator(lista , 15)
            
            try:
                location = paginator.page(1)
            except EmptyPage:
                location = paginator.page(paginator.num_pages)
            
            c.update({'lista':location , 'form':form})             
                
            return render(request, 'google/lista.html', c)

            
    elif request.GET and request.session.has_key('consulta'):
        if request.session.has_key('conta'):
            lista = LocationHistory.objects.filter(conta__icontains = request.session.get('conta'))
        if request.session.has_key('periodo'):
            if lista is None:
                lista = LocationHistory.objects.filter(turno = request.session.get('periodo'))
            else:
                lista = lista.filter(turno = request.session.get('periodo')) 
        if request.session.has_key('wifi') and not request.session.has_key('cell'):
            if lista is None:
                lista = LocationHistory.objects.filter(origem = 'WIFI')
            else:
                lista = lista.filter(origem = 'WIFI')
        elif  request.session.has_key('cell') and not request.session.has_key('wifi'):
            if lista is None:
                lista = LocationHistory.objects.filter(origem = 'CELL')
            else:
                lista = lista.filter(origem = 'CELL')
        if request.session.has_key('dtInicio') and request.session.has_key('dtFim'):
            inicio = datetime.strptime(request.session['dtInicio'], '%d/%m/%Y').date()
            fim = datetime.strptime(request.session['dtFim'], '%d/%m/%Y').date()
            
            if lista is None:
                lista = LocationHistory.objects.filter(data__range=(inicio, fim))
            else:
                lista = lista.filter(data__range=(inicio, fim))

                        
        paginator = Paginator(lista , 15)
        page = request.GET.get('page')
            
        try:
            location = paginator.page(page)
        except EmptyPage:
            location = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            location = paginator.page(1)
            
        c.update({'lista':location , 'form':form})             
                
        return render(request, 'google/lista.html', c)            
            
        
        
    
    
    lista = LocationHistory.objects.order_by('dataCriacao')
    
    paginator = Paginator(lista , 15)
    page = request.GET.get('page')
    
    try:
        location = paginator.page(page)
    except PageNotAnInteger:
        location = paginator.page(1)
    except EmptyPage:
        location = paginator.page(paginator.num_pages)
    
    c.update({'lista':location , 'form':form})
    return render(request, 'google/lista.html', c)

def listarnovo(request):
    """
    Lembrar de fazer as alterações para buscar objetos relacionados a pessoa
    """
    c= {}
    c.update(csrf(request))
    
    lista = LocationHistory.objects.order_by('-dataCriacao')
    
    paginator = Paginator(lista , 15)
    page = request.GET.get('page')
    
    try:
        location = paginator.page(page)
    except PageNotAnInteger:
        location = paginator.page(1)
    except EmptyPage:
        location = paginator.page(paginator.num_pages)
    
    c.update({'lista':location })
    return render(request, 'google/lista_novo.html', c)




class ListarDados(generic.ListView):
    template_name='google/lista.html'
    context_object_name = 'lista'
    
    def get_queryset(self):
        return LocationHistory.objects.order_by('-dataCriacao')
    
