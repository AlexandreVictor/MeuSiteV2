from django.db import models
from datetime import datetime


# Create your models here.

class autor (models.Model):

    nome_autor = models.CharField(max_length=200)
    codigo = models.IntegerField()

    
    def __str__(self):
        #return self.nome_autor
        return self.nome_autor
    
    def __str__(self):
        #return self.nome_autor
        return '%s - %s' % (self.nome_autor, self.codigo)

class cadastro (models.Model):


    fk_autor=models.ForeignKey(autor, on_delete=models.CASCADE)
    reu = models.CharField(max_length=200)
    documento = models.CharField(max_length=14)
    rua = models.CharField(max_length=200)
    numero = models.IntegerField(null=True)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    complemento = models.CharField(max_length=200, null=True,blank=True)
    cep = models.CharField(max_length=8)
    numero_processo = models.IntegerField()
    segredo = models.IntegerField(default=0 ,verbose_name='Segredo ?')
    advogado= models.IntegerField(default=0 ,verbose_name='Tem advogado ?')
    data_inclusao = models.DateTimeField(auto_now=True, verbose_name ='Incluido em')
    fk_conta =  models.IntegerField(default=0)
    
    def __str__(self):
        return self.reu
class statusgeral (models.Model):

    STATUS_ACOMPANHAMENTO = (
        (1,"Teste - 1"),
        (2,"Teste - 2"),
        (3,"Teste - 3"),
        (4,"Teste - 4"),
        (5,"Teste - 5")
    )

    fk_cadastro = models.ForeignKey(cadastro, on_delete=models.CASCADE)
    data_alteracao = models.DateTimeField(auto_now=True)
    status_acompanhamento = models.IntegerField(choices=STATUS_ACOMPANHAMENTO, default=1) 
