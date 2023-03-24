#Conecta ao MSSQL Server

import pyodbc as pyodbc
import pandas as pd
import pprint as pprint



# Conectar ao banco de dados usando o driver ODBC
server = 'LAPTOP-6L4CV4JD\\SQLEXPRESS'
database = 'CPFGTS'
trusted_connection = 'yes'  # ou 'true' = Usa o logon integrado do windows

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=' + server + ';'
                      'DATABASE=' + database + ';'
                      'Trusted_Connection=' + trusted_connection + ';')

mycursor = conn.cursor()


with open('C:\\PROJETOS DEV\\SQL\\CPFGTS[1099].txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        if linha:
            mycursor.execute(f"SELECT * FROM [dbo].[AMOSTRA] WHERE [DEMONSTRATIVO] = {linha}")
            results = mycursor.fetchall()
            for row in results:
                print(row)
                with open('C:\\PROJETOS DEV\\SQL\\CPFGTS_NEW.txt', 'a') as outfile:
                    outfile.write(f'{row}\n')

conn.close()

