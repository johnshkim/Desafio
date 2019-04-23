from django.db import models

#criacao da model Cadastro( nome, link e preco)
class Cadastro(models.Model):
    nome = models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    preco = models.FloatField()
    def __str__(self):
        return self.nome