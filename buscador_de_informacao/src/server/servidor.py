import MySQLdb
from flask import Flask, jsonify

app = Flask(__name__)

def get_db_connection():
    try:
        conn = MySQLdb.connect(
                host='localhost',
                user='root',
                password='@Myn051021',
                database='dev_teste_de_nivelamento'  # O nome do banco de dados
        )
        return conn
    except MySQLdb.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None

print('conexao bem sucedida')

@app.route('/api/operadores', methods=['GET'])
def get_operadores():
    conn = get_db_connection()  # Conecta ao banco de dados
    if conn is None:
        return jsonify({"erro": "Não foi possível conectar ao banco de dados"}), 500

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM relatorio_cadop')  # Altere para a tabela correta
    operadores = cursor.fetchall()
    conn.close()

    return jsonify(operadores)

if __name__ == '__main__':
    app.run(debug=True)
