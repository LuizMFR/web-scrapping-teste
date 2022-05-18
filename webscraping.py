import requests
from bs4 import BeautifulSoup

url = 'https://publicacoes.estadao.com.br/guia-da-faculdade/page/1/?post_type=faculdades_2021&ano=2021&s=una&tipo=&modalidade=&estado=MG&cidade=Belo+Horizonte&classificacao='
page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.find('div', class_='listagem-faculdades').text)
