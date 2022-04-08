from django.db import models
 
class Servico(models.Model):
    nome_servico = models.CharField(max_length=60)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    descricao = models.TextField('Descrição', blank= True)
    creation_date = models.DateTimeField('Criado em')

    
    def __str__(self):
        return self.nome_servico