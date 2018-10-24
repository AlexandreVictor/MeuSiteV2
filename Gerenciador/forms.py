# -*- coding: utf-8 -*-
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *
from .models import *

class CadProcessoForm(forms.ModelForm):
    class Meta:
        model = cadastro
        exclude = ['data_inclusao','numero']
        labels = {
                 'fk_autor' : 'Autor do Processo',
                 'reu' : 'Nome do Réu',
                 'documento' : 'Cpf/Cnpj',

        }


    helper = FormHelper()
    helper.form_id = 'id-RelatorioForm'
    helper.form_method = 'post'
    #helper.form_class = 'post-form'
    #Remove o label 
    #helper.form_show_labels = False
    form_style = 'inline'
    helper.layout = Div(''
                        ,Div('',
                            Field('fk_autor',label = "whatever"  )
                            ,css_class = 'form-group col-md-3')
                        ,Div('',
                            Field('reu', )
                            ,css_class = 'form-group col-md-3')
                          ,Div('',
                            Field('documento', )
                            ,css_class = 'form-group col-md-2')
                    ,css_class = 'form-row')
                    



'''  <div class="form-row">
    <div class="form-group col-md-6">
      <label for="inputEmail4">Email</label>
      <input type="email" class="form-control" id="inputEmail4" placeholder="Email">
    </div>
    <div class="form-group col-md-6">
      <label for="inputPassword4">Password</label>
      <input type="password" class="form-control" id="inputPassword4" placeholder="Password">
    </div>
  </div>                    '''