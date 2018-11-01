from django.urls import path
from django.conf.urls import  url, include
from . import views
from Gerenciador.views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('CadastroProcesso', views.FrmCadastro, name='FrmCadastro'),
   # path('ListaProcesso', views.List_Processo, name='List_Processo'),
    url(r'^ListaProcesso$',Lista_Processo.as_view(), name='List_Processo'),


]