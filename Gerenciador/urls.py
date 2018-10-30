from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('CadastroProcesso', views.FrmCadastro, name='FrmCadastro'),
    path('ListaProcesso', views.List_Processo, name='List_Processo'),


]