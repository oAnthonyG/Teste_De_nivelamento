import wget
import requests
from bs4 import BeautifulSoup
import zipfile

link_site = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

requisicao = requests.get(link_site)
site = BeautifulSoup(requisicao.text, "html.parser")

pesquisas = site.find_all('a')
pdf_links = [link.get('href') for link in pesquisas if 'pdf' in link.get('href', '') and ('Anexo_I' in link.get('href', '') or 'Anexo_II' in link.get('href', ''))]

arquivos_baixados = []
for nome_arquivo in pdf_links:
  nome_arquivo_local = nome_arquivo.split("/")[-1]
  print(f"baixando {nome_arquivo_local}")
  wget.download(nome_arquivo)
  arquivos_baixados.append(nome_arquivo_local)

with zipfile.ZipFile('Anexos.zip', 'w') as zipf:
  for pdf in arquivos_baixados:
    zipf.write(pdf, pdf)
