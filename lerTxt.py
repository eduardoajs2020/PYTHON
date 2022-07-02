# r= read(ler)
# w= write(escrever)
# a= append(incrementar)
# x= criar arquivo
# rw= leitura e escrita


with open('manipular textos.txt ', 'r') as arquivo:
    mercadinho = arquivo.readlines()
    print(mercadinho)
    arquivo.close()
