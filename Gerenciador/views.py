##http://pythonclub.com.br/class-based-views-django.html
##http://mindbending.org/pt/customizando-a-autenticacao-de-usuarios-no-django-19
import datetime
from .forms import *
from .models import *
from django.urls import reverse, reverse_lazy, resolve
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.db.models import Q
from django.views.generic import CreateView, ListView, DetailView
# Create your views here.

#@login_required
# ---------------------------- CADASTRO DE PROCESSOS 
class  CadastroProcessoView(CreateView):
    model = cadastro
    form_class = Frm_Cadastro_Processo
    template_name = 'Gerenciador/Frm_Cad_Processo.html'
    #success_url = reverse_lazy('Lista_Processo')

    def get_success_url(self, **kwargs):
        return reverse('StatusProcesso', kwargs={'pk': self.object.pk})
# ---------------------------- CADASTRO DE PROCESSOS STATUS DO PROCESSO
class  StatusProcessoView(CreateView):
    model = statusgeral
    form_class = Frm_Status_Processo
    template_name = 'Gerenciador/Frm_Status_Processo.html'
    success_url = reverse_lazy('ListaProcesso')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cadastro_pk = self.kwargs['pk']
        cadastro_list = cadastro.objects.get(pk=cadastro_pk)
        context.update({
            'cadastro_list': cadastro_list
        })
        return context

    def form_is_invalid(self, form):
        print(form.data)
        return super().form_valid(form)

    def form_valid(self, form):
        form.instance.fk_cadastro_id = self.kwargs.get('pk') #self.kwargs['pk']
        print(form.data)
        return super().form_valid(form)
# ---------------------------- DETALHES DE PROCESSOS
class DetalhesProcessoView(DetailView):
    model = statusgeral
    template_name = 'Gerenciador/Detalhe_Processo.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cadastro_pk = self.kwargs['pk']
        cadastro_list = cadastro.objects.get(pk=cadastro_pk)
        statusgeral_list = statusgeral.objects.all().filter(fk_cadastro_id=cadastro_pk)
        context.update({
            'cadastro_list': cadastro_list,
            'statusgeral_list': statusgeral_list
        })
        return context

# ---------------------------- LISTA DE PROCESSOS
class ListaProcessoView(ListView):
    model = cadastro
    template_name ='Gerenciador/Lista_Processo.html'
    paginate_by = 15 
 

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
        context = super(ListaProcessoView, self).get_context_data(**kwargs)
        context['Autor']  = autor.objects.select_related('fk_autor').values()
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