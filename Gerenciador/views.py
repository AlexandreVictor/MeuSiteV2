from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import *
from .models import *
from django.shortcuts import redirect
from django.views.generic import CreateView,ListView
# Create your views here.

class Lista_Processo(ListView):
    model = cadastro
    template_name ='Gerenciador/Lista_Processo.html'
    paginate_by = 10
   # context_object_name = 'resultados'

    def get_queryset(self, **kwargs):
        print('teste')
        filtro1 = self.request.GET.get('bairro', '')
        return cadastro.objects.filter(bairro__icontains=filtro1,)

    def get_context_data(self, **kwargs):
        context = super(Lista_Processo, self).get_context_data(**kwargs)
        context['bairro'] = self.request.GET.get('bairro', '')
        #context['meuform'] = MeuForm
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