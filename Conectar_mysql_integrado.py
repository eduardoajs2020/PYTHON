#Conecta ao Mysql

import pymysql as pymysql

import os as os

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='10205618',
                       db='dicionario_ti',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor,
                       autocommit=True,
                       use_unicode=True,
                       named_pipe=False)



mycursor = conn.cursor()

#Execute a query
mycursor.execute("SELECT * FROM dicionario")

# Fetch the results
results = mycursor.fetchall()

# Print the results
for row in results:
    
    print(row)

# Close the connection
conn.close()
