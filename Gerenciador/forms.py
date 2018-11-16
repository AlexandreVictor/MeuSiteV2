# -*- coding: utf-8 -*-
from django import forms
from Gerenciador.models import *
class Frm_Cadastro_Processo(forms.ModelForm):
    
    segredo = forms.RadioSelect()
    advogado = forms.RadioSelect()
    complemento = forms.CharField(required = False)
    class Meta:
        model = cadastro
    # Campos que estarão no form
        fields = '__all__'
        exclude = ['data_inclusao','fk_conta']

class Frm_Status_Processo(forms.ModelForm):
     
    notas = forms.CharField(required = False, widget=forms.Textarea)
    
    class Meta:
        model = statusgeral
    # Campos que estarão no form
        fields = '__all__'
        exclude = ['data_alteracao','fk_cadastro']
