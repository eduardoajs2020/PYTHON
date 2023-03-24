#Conecta ao MSSQL Server

import pyodbc as pyodbc
import pandas as pd
import pprint as pprint



# Conectar ao banco de dados usando o driver ODBC
server = 'LAPTOP-6L4CV4JD\\SQLEXPRESS'
database = 'DIO_MAIO'
trusted_connection = 'yes'  # ou 'true' = Usa o logon integrado do windows

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=' + server + ';'
                      'DATABASE=' + database + ';'
                      'Trusted_Connection=' + trusted_connection + ';')

mycursor = conn.cursor()


with open('C:\\PROJETOS DEV\\SQL\\CODIGO.txt', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        if linha:
            mycursor.execute (f"SELECT DISTINCT * FROM dbo.PRODUTOS WHERE CODIGO = {linha}")
            results = mycursor.fetchall()

            with open('C:\\PROJETOS DEV\\SQL\\CODIGO_NEW.txt', 'a') as outfile:
                    for row in results:
                        row = [str(val).strip() 
                               if type(val) is str 
                               else val for val in row]

                    #  Formatar a coluna de data se ela existir
                        if row[2] is not None:
                            date_str = row[2].strftime('%d/%m/%Y')
                        else:
                            date_str = ''

                    # Concatenar os valores de cada coluna junto com as guias
                    row_str = ', '.join(
                    [str(col) for col in [row[0], row[1], date_str, row[3], row[4]]])
                    outfile.write(row_str + '\n')
                    print(row_str)

conn.close()

