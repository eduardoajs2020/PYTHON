"""
for in Python
iterando strings com for
Função range (star=0, stop, step=1)
"""

for x in range(0, 100, 8):
    print(x)

print('1####################################1')

for n in range(100):
    if n % 8 == 0:
        print(n)

print('2####################################2')
for m in range(0, 100, 3):
    print(m)

print('3####################################3')
for m in range(100):
    if m % 3 == 0:
        print(m)

texto = 'python'
nova_string = ''

for letra in texto:
    if letra == 't':
        # continue
        # break
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

        print(nova_string)
