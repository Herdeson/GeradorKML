# -*- coding: utf-8 -*-
'''
Created on 26/06/2015

@author: herdeson
'''
from django import forms


TURNO = (
           ('1', 'Manhã'),
           ('2', 'Tarde'),
           ('3', 'Noite'),
           ('4', 'Madrugada'),
           )

class UploadCvs(forms.Form):
    arquivo = forms.FileField()
    
class FiltroForm(forms.Form):
    conta = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    periodo = forms.ChoiceField(required=False, choices=TURNO, widget=forms.Select(attrs={'class': 'form-control'}))
    wifi = forms.BooleanField(required=False, label='WIFI')
    cell = forms.BooleanField(required=False, label='CELL' )
    dtInicio = forms.DateField(required=False, input_formats=['%d/%m/%Y'] , widget= forms.DateInput(attrs={'class': 'form-control'}))
    dtFim = forms.DateField(required=False, input_formats=['%d/%m/%Y'], widget= forms.DateInput(attrs={'class': 'form-control'}))
    