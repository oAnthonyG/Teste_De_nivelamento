import wget
import requests
from bs4 import BeautifulSoup

link_site = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

requisicao = requests.get(link_site)
print(requisicao)

site = BeautifulSoup(requisicao.text, "html.parser")

pesquisa = site.find_all("a", class_="internal-link")

print(pesquisa[0])
# link = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
# wget.download(link, 'anexo1.pdf')