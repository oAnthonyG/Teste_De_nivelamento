# Teste de Nivelamento

Este repositório contém as respostas de um teste de nivelamento, como o próprio nome sugere. Aqui, contém as soluções para os testes realizados, com o intuito de demonstrar o meu conhecimento sobre os tópicos abordados. Agradeço pela oportunidade de participar deste desafio, que me permitiu aprimorar minhas habilidades e colocar à prova o que aprendi até agora.

Esse processo tem sido muito enriquecedor, pois me permitiu entender melhor minhas áreas de força e também onde posso melhorar. Espero que este repositório sirva como uma demonstração clara do meu aprendizado, capacidade e dedicação ao longo dessa jornada.

---

## Teste de Web Scraping

Neste teste, criei um script em Python para realizar a seguinte tarefa:

- Acessar um link específico.
- Fazer o download de dois arquivos PDF específicos.
- Compactar os arquivos PDF em um único arquivo ZIP.

**Ferramentas utilizadas:**
- **Linguagem:** Python
- **Bibliotecas:** 
  - Wget        
  - Requests
  - BeautifulSoup
  - ZipFile
  - Para a instalação das Blibliotecas é nessario digitar no Terminal Pip install 'nome da biblioteca'

Arquivo: `teste_web-scraping.py`

---

## Teste de Transformação de Dados

Neste teste, criei um script em Python para realizar a seguinte tarefa:

- Extrair os dados de uma tabela chamada **"Rol de Procedimentos e Eventos em Saúde"** de um arquivo PDF.
- Salvar os dados extraídos em um arquivo `.csv`.
- Compactar o arquivo `.csv` em um arquivo ZIP.

**Ferramentas utilizadas:**
- **Linguagem:** Python
- **Bibliotecas:** 
  - Tabula
  - ZipFile
  - Para a instalação das Blibliotecas é nessario digitar no Terminal Pip install 'nome da biblioteca'

Arquivo: `teste_de_transformacao_de_dados.py`

---

## Teste de Banco de Dados

Neste teste, após baixar arquivos específicos manualmente, criei um script SQL para:

- Criar tabelas estruturadas no banco de dados para aceitar a importação dos dados dos arquivos.
- Utilizar o **DBeaver**, que é uma ferramenta de gerenciamento de banco de dados, para executar o script.

**Ferramentas utilizadas:**
- **Ferramenta de Banco de Dados:** DBeaver
- **Linguagem:** SQL

Arquivo: `teste_de_banco_de_dados.sql`

---

## Teste de Banco de Dados

Neste teste, desenvolvi um sistema que consiste em uma interface web interativa utilizando Vue.js, conectada a um servidor backend escrito em Python. O objetivo foi criar uma API que acessa um banco de dados gerenciado no DBeaver e exibe os dados na interface.

**Ferramentas utilizadas:**

- **Linguagem:** Python (Flask)

- **Banco de Dados:** SQL (Gerenciado no DBeaver)

- **Linguagem Frontend:** JavaScript (Vue.js)

Arquivos: `buscador_de_informacao` (Código da interface web)
          `servidor.py`             (Script do servidor)


**Instalando o Vue.js**

Para instalar o Vue.js e configurar um novo projeto, siga os passos abaixo:

1. Instale o Node.js (se ainda não tiver instalado)
  [:Download do Node.js](https://nodejs.org/)

2. Instale o Vue CLI globalmente:
```bash
npm install -g @vue/cli
```

3. Acesse a pasta do projeto existente e instale as dependências:
```bash
cd buscador_de_informacao
npm install
```

4. Inicie o servidor do Vue.js:
```bash
npm run dev
```

**Instalando as Bibliotecas Python Necessárias**
Para instalar as bibliotecas usadas no backend, utilize o seguinte comando:
```bash
pip install MySQLdb Flask Flask-Cors
pip install jsonify make_response
```

**Executando o Projeto**

1. Executar o backend (API Flask):
```bash
cd src/server
python server.py
```

2. Executar o frontend (Vue.js):
```bash
cd buscador_de_informacao
npm run dev
```
3. Acessar o projeto no navegador:

- O backend rodará em http://127.0.0.1:5000
- O frontend rodará em http://localhost:5317