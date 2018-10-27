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