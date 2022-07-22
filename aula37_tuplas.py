
#  diferença entre tupla() e lista[]: na tupla não dá para modificar os elementos

t1 = 1, 2, 3, 4, 5
print(t1)

t1 = list(t1)  # transforma tupla em lista
print(t1)

t1[1] = 3000  # inclui elemento
print(t1)

t1 = tuple(t1)  # reverte para tupla
print(t1)

