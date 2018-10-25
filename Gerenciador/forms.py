# -*- coding: utf-8 -*-
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *
from .models import *

class CadProcessoForm(forms.ModelForm):
    class Meta:
        model = cadastro
        exclude = ['data_inclusao']
        labels = {
                 'fk_autor' : 'Autor do Processo',
                 'reu' : 'Nome do Réu',
                 'documento' : 'Cpf/Cnpj',
                 'advogado' : 'Possui Advogado ?',
                 'segredo':'É segredo ?'

        }


    helper = FormHelper()
    helper.form_id = 'id-RelatorioForm'
    helper.form_method = 'post'
    #helper.form_class = 'post-form'
    #Remove o label 
    #helper.form_show_labels = False
    form_style = 'inline'
    helper.layout = Layout (Div(''
                                ,Div('',
                                        Field('fk_autor', )
                                       ,css_class = 'form-group col-md-4')
                                ,Div('',
                                        Field('reu', )
                                        ,css_class = 'form-group col-md-5')
                                ,Div('',
                                        Field('documento', )
                                        ,css_class = 'form-group col-md-2')
                            ,css_class = 'form-row'),
                            Div(''
                               ,Div('',
                                       Field('rua',)
                                      ,css_class = 'form-group col-md-6')
                               ,Div('',
                                       Field('numero',)
                                      ,css_class = 'form-group col-md-2')
                               ,Div('',
                                       Field('complemento',)
                                      ,css_class = 'form-group col-md-4')                                                                             
                            ,css_class = 'form-row'),
                            Div(''
                               ,Div('',
                                       Field('bairro',)
                                      ,css_class = 'form-group col-md-3')
                               ,Div('',
                                       Field('cidade',)
                                      ,css_class = 'form-group col-md-4')
                               ,Div('',
                                       Field('cep',)
                                      ,css_class = 'form-group col-md-4')                                                                             
                            ,css_class = 'form-row'),
                            Div('',
                                Field('segredo',type ='radio', id ='1',css_class = 'btn btn-secondary' ),  #css_class='btn btn-secondary')
                                Field('segredo',type ='radio', id ='2',css_class = 'btn btn-secondary' )  #css_class='btn btn-secondary')
                            ,css_class="btn-group btn-group-toggle" #data-toggle="buttons"
                            ),
                            Div('',
                                Div('',
                                       Field('advogado',)
                                      ,css_class = 'form-group col-md-4')
                            ,css_class = 'btn-group btn-group-toggle'),
                            ButtonHolder(
                                Submit('submit', 'Salvar', css_class='btn btn-success'),
                                Submit('cancel', 'Cancelar', css_class='btn btn-danger')),
                            )

''' 

  <div class="btn-group btn-group-toggle" data-toggle="buttons">
  <label class="btn btn-secondary active">
    <input type="radio" name="options" id="option1" autocomplete="off" checked> Active
  </label>
  <label class="btn btn-secondary">
    <input type="radio" name="options" id="option2" autocomplete="off"> Radio
  </label>
  <label class="btn btn-secondary">
    <input type="radio" name="options" id="option3" autocomplete="off"> Radio
  </label>
</div>

<div class="btn-group btn-group-toggle" > 
    <div class="form-group">
     <div id="div_id_segredo" class="form-check">
         <label for="1" class="form-check-label"> 
         <input type="checkbox" name="segredo" class="btn btn-secondary checkboxinput form-check-input" type="radio" id="1">
                    É segredo ?
         </label> 
        </div> 
    </div> 


 '''