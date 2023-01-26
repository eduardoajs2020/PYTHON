

# um dicionário deve possuir uma chave e um valor e, fica entre chaves{}

d1 = {1: 'a', 2: 'b'}
v = d1.copy()
print(d1)
print(v)

print('===========================================================================')

dic1 = {'chave1': 'valor da chave'}

print(dic1)

print('===========================================================================')

dic1['nova_chave'] = 'valor da nova chave'

print(dic1['chave1'])

print('===========================================================================')

dic2 = dict(chave1='valor da chave', chave2='valor da outra chave')
dic2['nova_chave'] = 'valor da nova chave'

print(dic2['chave1'])

print('===========================================================================')
# mistos

dicio1 = {
    'str': 'valor',
    123: 'Outro valor',
    (1, 2, 3, 4): 'Tupla',
}

print(dicio1[(1, 2, 3, 4)])

print('===========================================================================')

dicio2 = {'str': 'valor', 135: 'Outro valor', (1, 2, 3, 4): 'Tupla', 'naoexiste': 'Agora existe.'}

if 'naoexiste' in dicio2:
    print(dicio2['naoexiste'])

print('===========================================================================')

dicio3 = {
    'str': 'valor',
    123: 'Outro valor',
    (1, 2, 3, 4): 'Tupla',
}
print('str' in dicio3)
print('str' in dicio3.keys())
print('valor' in dicio3.values())

print('===========================================================================')

dicio3 = {
    'str': 'valor',
    123: 'Outro valor',
    (1, 2, 3, 4): 'Tupla',
}
print(len(dicio3))

for k in dicio3.items():  # items acessa chave e valor
    print(k)

print('===========================================================================')

d2 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Luiz', 'Otavio']}
v1 = d2.copy()

v1[1] = 'Luiz'

print(v1['d'][0])

print(d2)
print(v1)


print('===========================================================================')
