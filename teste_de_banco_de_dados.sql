create database dev_teste_de_nivelamento; # Criado o Banco de dados
use dev_teste_de_nivelamento;             # Entrando no banco de dados

CREATE table Registro_Trimestral(
	DATA date NOT NULL,
	REG_ANS int NOT NULL,
	CD_CONTA_CONTABIL int,
	DESCRICAO varchar(255),
	VL_SALDO_INICIAL INT NOT NULL,
	VL_SALDO_FINAL INT NOT NULL
);                                       #Criado uma tabela chamada 'Registro_Trimestral'

LOAD DATA INFILE "C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\1T2023.csv"  #Tive que adicionar um arquvio de cada vez manualmente
INTO TABLE  registro_trimestral
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;                           #Comando para importar o conteudo do arquivo csv
                                          # Para o banco de dados Registro_Trimestral


select
	data,
	REG_ANS,
	CD_CONTA_CONTABIL,
	DESCRICAO,
	VL_SALDO_FINAL
from
Registro_Trimestral
where
	DESCRICAO like 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
	and data '2024-01-01' 
order by
	VL_SALDO_FINAL  desc
limit 10;                                     # Filtragem para saber quais as 10 operadoras com maiores despesas
                                              # No ultimo trimestre

select
	data,
	REG_ANS,
	CD_CONTA_CONTABIL,
	DESCRICAO,
	VL_SALDO_FINAL
from
	Registro_Trimestral
where
	DESCRICAO like 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
	and data between '2024-01-01' and '2024-10-01' 
order by
	VL_SALDO_FINAL  desc
limit 10;                                        # Filtragem para saber quais as 10 operadoras 
                                                  # com maiores despesas nessa categoria no último ano                              



CREATE table relatorio_cadop (
	Registro_ANS int,
	CNPJ bigint(14) NOT NULL,
	Razao_Social varchar(255) NOT NULL,
	Nome_Fantasia varchar(80) NOT NULL,
	Modalidade varchar(255) NOT NULL,
	Logradouro varchar(150) NOT NULL,
	Numero varchar(20),
	Complemento varchar(255),
	Bairro varchar(50) NOT NULL,
	Cidade varchar(50) NOT NULL,
	UF char(3) NOT NULL,
	CEP int(8) NOT NULL,
	DDD int(2),
	Telefone varchar(20),
	Fax varchar(20),
	Endereco_eletronico varchar(100) NOT NULL,
	Representante varchar(255) NOT NULL,
	Cargo_Representante varchar(255)NOT NULL,
	Regiao_de_Comercializacao tinyint,
	Data_Registro_ANS varchar(10) NOT NULL
  );                                                         #Criado a tabela Relatorio_Cadop

