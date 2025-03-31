import MySQLdb
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS

app = Flask(__name__)

CORS(app, origins='http://localhost:5173', methods=['GET'], allow_headers=['Content-Type'])

conexao = MySQLdb.connect(
    host='localhost',
    user='root',
    password='@Myn051021',
    database='dev_teste_de_nivelamento'

)

print('conexao bem sucedida')


query = "select * from relatorio_cadop where Cargo_Representante like 'DIRETOR' order by Registro_ANS desc"

@app.route('/api', methods=['GET'])
def obter_dados():
  cursor = conexao.cursor()
  cursor.execute("select * from relatorio_cadop where Cargo_Representante like 'DIRETOR' order by Registro_ANS desc")
  minha_api = cursor.fetchall()
  conexao.close()

  relatorios = []
  for relatorio in minha_api:
    relatorios.append(
        {
            "Registro_ANS": relatorio[0],
            "CNPJ": relatorio[1] ,
            "Razao_Social": relatorio[2] ,
            "Nome_Fantasia": relatorio[3] ,
            "Modalidade": relatorio[4] ,
            "Logradouro": relatorio[5] ,
            "Numero": relatorio[6] ,
            "Complemento": relatorio[7] ,
            "Bairro": relatorio[8] ,
            "Cidade": relatorio[9] ,
            "UF": relatorio[10] ,
            "CEP": relatorio[11]  ,
            "DDD": relatorio[12] ,
            "Telefone": relatorio[13],
            "Fax varchar": relatorio[14],
            "Endereco_eletronico": relatorio[15],
            "Representante": relatorio[16],
            "Cargo_Representante": relatorio[17],
            "Regiao_de_Comercializacao": relatorio[18],
            "Data_Registro_ANS": relatorio[19]
        }
    )

  return make_response(jsonify(relatorios))




app.run(port=5000, host='localhost',debug=True)



