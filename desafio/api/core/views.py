from django.shortcuts import render
from rest_framework import viewsets
from .models import Cadastro
from .serializer import CadastroSerializer

#busca dos itens do cadastro no banco de dado
class CadastroViewSet(viewsets.ModelViewSet):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer
