# -*- coding: utf-8 -*-
from django import forms
from .models import *
class Cad_Form(forms.ModelForm):
    
    segredo = forms.RadioSelect()
    advogado = forms.RadioSelect()
    complemento = forms.CharField(required = False)
    class Meta:
        model = cadastro
    # Campos que estarão no form
        fields = '__all__'
        exclude = ['data_inclusao','fk_conta']

class ValidaDados(forms.Form):

    def verificaProcesso(**kwargs):
        
        numero_processo = kwargs.get('numero_processo')

        processoexiste = cadastro.objects.filter(numero_processo=numero_processo).exists()
        if processoexiste:
            print("processo já existe")
            return False
        else:
            return True

