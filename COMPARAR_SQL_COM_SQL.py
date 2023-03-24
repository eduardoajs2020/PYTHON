#COMPARA SQL COM SQL

import pandas as pd
import pyodbc as pyodbc
from sqlalchemy import create_engine

# Configurar a conexão com o banco de dados
server = 'LAPTOP-6L4CV4JD\\SQLEXPRESS'
database = 'Ecomerce'
trusted_connection = 'yes'  # ou 'true' = Usa o logon integrado do windows

conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection};'
conn = pyodbc.connect(conn_str)
engine = create_engine(f'mssql+pyodbc://', creator=lambda: conn)

# Executar as querys SQL
query1 = 'SELECT [Codigo] ,[Nome],[TipoPessoa]FROM [dbo].[Clientes]'
query2 = 'SELECT [Codigo] ,[Nome],[TipoPessoa]FROM [dbo].[Clientes]'
dados1 = pd.read_sql(query1, engine)
dados2 = pd.read_sql(query2, engine)

# Comparar os dados das duas tabelas
dados_repetidos = pd.merge(dados1, dados2, how='inner')

# Contar a quantidade de vezes que cada dado repetido aparece
contador = dados_repetidos.groupby(list(dados_repetidos.columns)).size().reset_index(name='ocorrencias')

# Escrever os dados repetidos em um arquivo TXT
contador.to_csv('dados_repetidos.txt', sep=',', index=False)

