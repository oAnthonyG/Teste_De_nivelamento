import wget
import requests
from bs4 import BeautifulSoup
import zipfile

url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

resposta_site = requests.get(url)
pagina_html = BeautifulSoup(resposta_site.text, "html.parser")

links_da_pagina = pagina_html.find_all('a')
links_pdf = [link.get('href') for link in links_da_pagina if 'pdf' in link.get('href', '') and ('Anexo_I' in link.get('href', '') or 'Anexo_II' in link.get('href', ''))]

nomes_arquivos_baixados = []
for link_pdf in links_pdf:
  nome_arquivo_local = link_pdf.split("/")[-1]
  print(f"Baixando {nome_arquivo_local}")
  wget.download(link_pdf)
  nomes_arquivos_baixados.append(nome_arquivo_local)

with zipfile.ZipFile('Rol De Procedimentos E Eventos Em Saude.zip', 'w') as arquivo_zip:
  for arquivo_pdf in nomes_arquivos_baixados:
    arquivo_zip.write(arquivo_pdf, arquivo_pdf)
