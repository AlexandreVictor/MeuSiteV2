from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import cadastro, autor


class CadProcessoForm(forms.ModelForm):
    class Meta:
        model = cadastro
        exclude = ['fk_autor','data_inclusao','numero']

    reu = forms.CharField(max_length=200,
                         label = "Réu do Processo",
                         required = True,)
    documento = forms.CharField(max_length=14,
                         label = "CPF/CNPJ",
                         required = True,)
    rua = forms.CharField(max_length=200,
                         label = "Endereço da Inicial - Rua",
                         required = True,)
    """numero = forms.IntegerField()
    bairro = forms.CharField(max_length=200)
    cidade = forms.CharField(max_length=200)
    complemento = forms.CharField(max_length=200)
    cep = forms.CharField(max_length=8)
    numero_processo = forms.IntegerField()
    #segredo = forms.IntegerField(default=0)
    segredo = forms.BooleanField()
    advogado= forms.BooleanField()
    data_inclusao = forms.DateTimeField()
    fk_conta =  forms.IntegerField()"""
    
    def __init__(self, *args, **kwargs):
        super(CadProcessoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-CadProcessoForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.add_input(Submit('submit', 'Submit'))