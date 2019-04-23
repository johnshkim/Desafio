import requests
from rest_framework import serializers
from bs4 import BeautifulSoup
from .models import Cadastro
#request- biblioteca do python que realiza o get da pagina (download deseuselementos)
page = requests.get('https://nerdstore.com.br/categoria/especiais/game-of-thrones/')
soup = BeautifulSoup(page.content, 'html.parser')
#Se odownloadfor realizado é retornado com status 200
#page.status_code
#exibir conteudo da pagina
#page.content
#buscar pela class
nome = soup.find_all('span', class_='ellip')
link = soup.find_all('img', class_='attachment-woocommerce_thumbnail size-woocommerce_thumbnail')
preco = soup.find_all('span', class_='woocommerce-Price-currencySymbol')
#print(nome, link, preco)
print(len(nome, link, preco))

class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastro
        fields = ('id', 'nome', 'link', 'preco')