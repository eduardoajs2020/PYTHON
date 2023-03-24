import pandas as pd
import pyodbc as pyodbc

# Conectar ao banco de dados usando o driver ODBC
server = 'LAPTOP-6L4CV4JD\\SQLEXPRESS'
database = 'DIO_MAIO'
trusted_connection = 'yes'  # ou 'true' = Usa o logon integrado do windows

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=' + server + ';'
                      'DATABASE=' + database + ';'
                      'Trusted_Connection=' + trusted_connection + ';')

mycursor = conn.cursor()

# Especificar o código e os anos desejados
codigo_desejado = (1, 2, 3, 4) # Para mais de um código, use uma tupla
ano_desejado = 2022

# Escrever a consulta SQL
query = f'''
SELECT 
    codigo, 
    MONTH(DATA_VALIDADE) as mes,
    SUM(CAST(CODIGO as FLOAT)) as TOTAL_CODIGO,
    SUM(CAST(EAN as FLOAT)) as TOTAL_EAN
FROM 
    dbo.PRODUTOS
WHERE 
    codigo IN {codigo_desejado} AND YEAR(DATA_VALIDADE) = {ano_desejado}  -- Alterar para o nome da coluna correta
GROUP BY 
    codigo, 
    MONTH(DATA_VALIDADE)
'''

# Ler a consulta SQL usando o pandas
df = pd.read_sql(query, conn)

# Ordenar o resultado pelo mês
df = df.sort_values(by=['mes'])

# Exportar o resultado para o Excel
nome_arquivo_excel = 'resultado.xlsx'
df.to_excel(nome_arquivo_excel, index=False)
