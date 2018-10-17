from django.contrib import admin

# Register your models here.
from .models import cadastro, autor
class cadastroAdmin(admin.ModelAdmin):

    model = cadastro


    fieldsets = [
        ('Dados Gerais', {'fields': ['fk_autor',(('reu','documento'))]}),
        ('Endereço da Inicial', {'fields': [(('rua','numero','bairro')),(('cidade','cep'))]}),
        ('Dados Processo', {'fields': [(('numero_processo', 'segredo','advogado'))]}),

    ]
    list_display = ['fk_autor','numero_processo', 'bairro','cidade','segredo','advogado','data_inclusao']
    list_filter = ['fk_autor', 'bairro', 'cidade','segredo','advogado']
    search_fields = [(('numero_processo'))]
   # save_on_top = True

admin.site.register(cadastro,cadastroAdmin)
admin.site.register(autor)