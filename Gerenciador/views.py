##http://pythonclub.com.br/class-based-views-django.html
import datetime
from django.urls import reverse, reverse_lazy, resolve
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.db.models import Q
from .forms import *
from .models import *
from django.shortcuts import redirect
from django.views.generic import CreateView,ListView
# Create your views here.

#@login_required
class  CadastroProcessoView(CreateView):
    model = cadastro
    form_class = Frm_Cadastro_Processo
    template_name = 'Gerenciador/Frm_Cad_Processo.html'
    #success_url = reverse_lazy('List_Processo')

    def get_success_url(self, **kwargs):
        return reverse('StatusProcesso', kwargs={'pk': self.object.pk})

class  StatusProcessoView(CreateView):
    model = statusgeral
    form_class = Fmr_Status_Processo
    template_name = 'Gerenciador/Frm_Status_Processo.html'
    success_url = reverse_lazy('List_Processo')
    def get_queryset(self, **kwargs):
        # Filtros Basicos 
        f_Autor = self.request.GET.get('pk')
        print(f_Autor)
        
        

    def get_context_data(self, **kwargs):
        context = super(StatusProcessoView, self).get_context_data(**kwargs)
        print('teste',self.request.GET.get('pk'))
        context['Autor']  = cadastro.objects.filter(pk=1).values()
        #context['bairro'] = self.request.GET.get('bairro', '')
        return context 


class Lista_Processo(ListView):
    model = cadastro
    template_name ='Gerenciador/Lista_Processo.html'

    def get_queryset(self, **kwargs):
        #Objeto Q ORM
        filtro_Basico = Q()
        filtro_Avancado = Q()

        # Filtros Basicos 
        f_Autor = self.request.GET.get('Autor')
        f_NumeroProcesso = self.request.GET.get('NumeroProcesso')
        f_DataInclusao = self.request.GET.get('DataInclusao')
        # Filtros Avançados
        f_Bairro = self.request.GET.get('Bairro','')
        f_Cidade = self.request.GET.get('Cidade','')
        f_Segredo = self.request.GET.get('Segredo','')
        f_Advogado = self.request.GET.get('Advogado','')


        if f_Autor is not None and f_Autor != 'Selecione Autor':
            filtro_Basico.add(Q(fk_autor=f_Autor), Q.AND)
        if f_NumeroProcesso:
            filtro_Basico.add(Q(numero_processo=f_NumeroProcesso), Q.AND)
        if f_DataInclusao:
            f_DataInclusao = datetime.strptime(f_DataInclusao, '%Y-%m-%d').date()
            filtro_Basico.add(Q(data_inclusao__date=f_DataInclusao), Q.AND)
        if filtro_Basico:
            return cadastro.objects.filter(filtro_Basico)

        if f_Bairro:
            filtro_Avancado.add(Q(bairro__icontains=f_Bairro), Q.AND)
        if f_Cidade:
            filtro_Avancado.add(Q(cidade__icontains=f_Cidade), Q.AND)
        if f_Segredo:
            filtro_Avancado.add(Q(segredo=f_Segredo), Q.AND)
        if f_Advogado:
            filtro_Avancado.add(Q(advogado=f_Advogado), Q.AND)
        if filtro_Avancado:
            return cadastro.objects.filter(filtro_Avancado)
        else:
            return cadastro.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(Lista_Processo, self).get_context_data(**kwargs)
        context['Autor']  = autor.objects.select_related('fk_autor').values()
        #context['bairro'] = self.request.GET.get('bairro', '')
        return context 

def index(request):
    context = {'teste' : None}
    return render(request, 'Gerenciador/base.html', context)


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