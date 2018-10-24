from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
# Create your views here.


def index(request):
    context = {'teste' : None}
    return render(request, 'Gerenciador/base.html', context)


def cadProcesso(request):
    #context = {'teste' : None}
    return render(request, 'Gerenciador/FormCad.html',{'CadProcessoForm': CadProcessoForm()})