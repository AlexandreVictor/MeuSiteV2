from django.urls import path
from django.conf.urls import  url, include
from . import views
from Gerenciador.views import *

urlpatterns = [
    path('', views.index, name='index'),
   # path('CadastroProcesso', views.FrmCadastro, name='FrmCadastro'),
   # path('ListaProcesso', views.List_Processo, name='List_Processo'),
    url(r'^ListaProcesso$',ListaProcessoView.as_view(), name='ListaProcesso'),
    url(r'^ListaProcesso/CadastroProcesso$',CadastroProcessoView.as_view(), name='CadastroProcesso'),
    url(r'^ListaProcesso/CadastroProcesso/StatusProcesso/(?P<pk>\d+)/$',StatusProcessoView.as_view(), name='StatusProcesso'),
    url(r'^ListaProcesso/Detalhe/(?P<pk>\d+)/$',DetalhesProcessoView.as_view(), name='DetalheProcesso'),

]