#Conecta ao MariaDB

import mysql.connector 
    

conn = mysql.connector.connect(host='localhost',
                               db='dicionario_ti',
                               user='root',
                               password='10205618'
                              )

if conn.is_connected():

   db_info = conn.get_server_info()

   print("Conectado ao servidor MySQL versao", db_info)


mycursor = conn.cursor()

mycursor.execute("SELECT * FROM dicionario")

result = mycursor.fetchall()


for row in result:

    print(row)

conn.close()
