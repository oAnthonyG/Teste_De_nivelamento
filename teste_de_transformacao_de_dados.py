import tabula
import zipfile
abreviacoes = {
  'OD': 'Seg. Odontológica',
  'AMB': 'Seg. Ambulatorial'
}

pdf_com_tabelas = tabula.read_pdf("Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf", pages="4")

df = pdf_com_tabelas[0]
df = df.rename(columns=abreviacoes)
df.to_csv('Rol_de_Procedimentos_e_Eventos_em_Saúde.csv', index=False)

with zipfile.ZipFile("Teste_Anthony_Guilherme.zip", "w") as zipf:
  zipf.write("Rol_de_Procedimentos_e_Eventos_em_Saúde.csv", arcname="Rol_de_Procedimentos_e_Eventos_em_Saúde.csv")

