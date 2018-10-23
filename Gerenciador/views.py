from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    context = {'teste' : None}
    return render(request, 'Gerenciador/base.html', context)