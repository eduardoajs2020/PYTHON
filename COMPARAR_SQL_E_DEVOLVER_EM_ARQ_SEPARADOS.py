#Compara 2 tabelas SQL e devolve em arquivos separados
import pandas as pd
import pyodbc as pyodbc
from sqlalchemy import create_engine

# Configurar a conexão com o banco de dados
server = 'LAPTOP-6L4CV4JD\\SQLEXPRESS'
database = 'DIO_MAIO'
trusted_connection = 'yes'  # ou 'true' = Usa o logon integrado do windows

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=' + server + ';'
                      'DATABASE=' + database + ';'
                      'Trusted_Connection=' + trusted_connection + ';')
engine = create_engine('mssql+pyodbc://', creator=lambda: conn)

# Executar as querys SQL
query1 = 'SELECT * FROM ESTOQUE'
query2 = 'SELECT * FROM PRODUTOS'
dados1 = pd.read_sql(query1, engine)
dados2 = pd.read_sql(query2, engine)

# Comparar os dados das duas tabelas
dados_repetidos = pd.merge(dados1, dados2, how='inner', indicator=True)

# Selecionar os dados que não se repetem na tabela ESTOQUE
dados_nao_repetidos_estoque = dados_repetidos[dados_repetidos['_merge'] == 'left_only'].drop('_merge', axis=1)

# Selecionar os dados que não se repetem na tabela PRODUTOS
dados_nao_repetidos_produtos = dados_repetidos[dados_repetidos['_merge'] == 'right_only'].drop('_merge', axis=1)

# Escrever os dados que não se repetem em um arquivo CSV
dados_nao_repetidos_estoque.to_csv('dados_nao_repetidos_estoque.txt', index=False)
dados_nao_repetidos_produtos.to_csv('dados_nao_repetidos_produtos.txt', index=False)
