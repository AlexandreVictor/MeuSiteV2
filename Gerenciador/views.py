from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import *
from .models import *
from django.shortcuts import redirect
# Create your views here.

def index(request):
    context = {'teste' : None}
    return render(request, 'Gerenciador/base.html', context)

def cadProcesso(request):

    if request.method == 'POST':
        form = CadProcessoForm(request.POST)
        if form.is_valid():
            Relatorios = form.save(commit=False)
            Relatorios = form.save()
            return redirect(index)
        else:
            form = CadProcessoForm()

    return render(request, 'Gerenciador/FormCad.html',{'form': CadProcessoForm()})


def FrmCadastro(request):
    errors = []
    if request.method == 'POST':
        form = Cad_Form(request.POST)
        dados = form.data
        Relatorios = form.save(commit=False)
        if Cad_Form.valida_nome(form, dados['nome_relatorio']) is False:
            print('Entrou no if')
            errors = []
            errors.append('O nome já está cadastrado')
            return render(request, 'GerenciadordeRotinas/Cad_Relatorio.html',{'form': Cad_Form(),'errors': errors})
    else:
        form = Cad_Form()
    return render(request, 'Gerenciador/Frm_Cad_Processo.html', {'form': Cad_Form()})