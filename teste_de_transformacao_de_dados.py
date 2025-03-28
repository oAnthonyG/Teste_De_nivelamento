import tabula
import zipfile
abreviacoes = {
  'OD': 'Seg. Odontológica',
  'AMB': 'Seg. Ambulatorial'
}

lista_tabelas = tabula.read_pdf("Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf", pages="4")

df = lista_tabelas[0]
df = df.rename(columns=abreviacoes)
df.to_csv('arquivo_csv_teste.csv', index=False)

with zipfile.ZipFile("Teste_Anthony_Guilherme.zip", "w") as zipf:
  zipf.write("arquivo_csv_teste.csv", arcname="arquivo_csv_teste.csv")

