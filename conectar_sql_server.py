#Conecta ao MSSQL Server

import pyodbc as pyodbc
import pprint as pprint


server = 'LAPTOP-6L4CV4JD\\SQLEXPRESS'
database = 'DIO_MAIO'
trusted_connection = 'yes'  # ou 'true' = Usa o logon integrado do windows


conn = pyodbc.connect ('DRIVER={ODBC Driver 17 for SQL Server};' 
                       'SERVER=' + server + ';' 
                       'DATABASE=' + database + ';'
                       'Trusted_Connection=' + trusted_connection + ';')


mycursor = conn.cursor()

mycursor.execute("SELECT * FROM dbo.PRODUTOS")

results = mycursor.fetchall()

for row in results:

    pprint.pprint(row)

conn.close()