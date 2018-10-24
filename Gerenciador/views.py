from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import *
from .models import *
from django.shortcuts import redirect
from django.views.generic import CreateView
# Create your views here.


def index(request):
    context = {'teste' : None}
    return render(request, 'Gerenciador/base.html', context)


#def cadProcesso(request):
    #context = {'teste' : None}
 #   return render(request, 'Gerenciador/FormCad.html',{'CadProcessoForm': CadProcessoForm()})

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