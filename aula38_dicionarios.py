import copy

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