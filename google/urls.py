'''
Created on 26/06/2015

@author: herdeson
'''
from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^importar', views.upload_CVS),
    url(r'^branco', views.branco , name='branco'),
    #url(r'^listar', views.ListarDados.as_view() , name='listarGoogle'),
    url(r'^listar_novo', views.listarnovo, name='listarNovo'),
    url(r'^listar', views.listarDados , name='listarGoogle'),
    
    
    
   
]