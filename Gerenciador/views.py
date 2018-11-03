##http://pythonclub.com.br/class-based-views-django.html
import datetime
import time
from datetime import timedelta

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from .forms import *
from .models import *

from django.shortcuts import redirect
from django.views.generic import CreateView,ListView
# Create your views here.

class Lista_Processo(ListView):
    model = cadastro
    template_name ='Gerenciador/Lista_Processo.html'
    #paginate_by = 10
   # context_object_name = 'resultados'
    def get_queryset(self, **kwargs):
        filtro_basico = Q()
        f_Autor = self.request.GET.get('Autor')
        f_NumeroProcesso = self.request.GET.get('NumeroProcesso')
        f_DataInclusao = self.request.GET.get('DataInclusao')
        string_date = "2018-08-30 17:00:00"
        format = "%Y-%m-%d %H:%M:%S"
        datainicio = datetime.datetime.strptime(string_date, format)
        #format = "%Y-%m-%d %H:%M:%S"
        #DataInclusao = datetime.datetime.strptime(f_DataInclusao, format)




        print(DataInclusao)
        print(type(DataInclusao))
        filtro1 = self.request.GET.get('bairro','')

        if f_Autor:
            filtro_basico.add(Q(fk_autor=f_Autor), Q.OR)
        if f_NumeroProcesso:
            filtro_basico.add(Q(numero_processo=f_NumeroProcesso), Q.OR)
        if f_DataInclusao:
            print('teste')
            
            #filtro_basico.add(Q(data_inclusao__gt=datetime.date(f_DataInclusao)), Q.OR)
        print(filtro_basico)
        if filtro_basico:
                  
            t = cadastro.objects.filter(filtro_basico)
            return t
        else:
            return cadastro.objects.filter(bairro__icontains=filtro1,).order_by('data_inclusao')

        
        #filtro2 = self.request.GET.get('advogado','')
        #return cadastro.objects.filter(bairro__icontains=filtro1,).order_by('data_inclusao')
        

    def get_context_data(self, **kwargs):
        context = super(Lista_Processo, self).get_context_data(**kwargs)
        context['Autor']  = autor.objects.select_related('fk_autor').values()
        context['bairro'] = self.request.GET.get('bairro', '')
        return context 

    

def index(request):
    context = {'teste' : None}
    return render(request, 'Gerenciador/base.html', context)

def List_Processo(request):
    processos_list = cadastro.objects.filter(fk_autor=1).order_by('data_inclusao')
    context = { 'processos_list' : processos_list}
    return render(request, 'Gerenciador/Lista_Processo.html', context)

def FrmCadastro(request):
    errors = []
    print(request.method)
    if request.method == 'POST':
        form = Cad_Form(request.POST)
        dados = form.data
        #print('Form é valido caralho ?',form.is_valid())
        if form.is_valid():
            form.save(commit=False)
            if ValidaDados.verificaProcesso(numero_processo = dados['numero_processo']) is False:
                errors.append("O processo já foi cadastrado")
                return render(request, 'Gerenciador/Frm_Cad_Processo.html', {'form': form,'errors':errors})
            #Salva o Form
            form.save()
            #Redireciona para pag
            return redirect(index)
    else:
       return render(request, 'Gerenciador/Frm_Cad_Processo.html', {'form': Cad_Form()})