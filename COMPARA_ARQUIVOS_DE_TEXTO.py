#COMPARA ARQUIVOS DE TEXTO

# Abrir os dois arquivos de texto
arquivo1 = open('arquivo1.txt', 'r')
arquivo2 = open('arquivoR.txt', 'r')

# Ler o conteúdo dos arquivos e armazená-los em variáveis
texto1 = arquivo1.read()
texto2 = arquivo2.read()

# Fechar os arquivos
arquivo1.close()
arquivo2.close()

# Quebrar o texto em palavras e armazená-las em listas
palavras1 = texto1.split()
palavras2 = texto2.split()

# Encontrar as palavras que aparecem em ambos os arquivos
palavras_repetidas = list(set(palavras1) & set(palavras2))

# Contar a quantidade de vezes que cada palavra repetida aparece
contador = {}
for palavra in palavras_repetidas:
    contador[palavra] = palavras1.count(palavra) + palavras2.count(palavra)

# Abrir um arquivo de saída para gravar as ocorrências repetidas
arquivo_saida = open('ocorrencias_repetidas.txt', 'w')

# Gravar as ocorrências repetidas no arquivo de saída
for palavra, ocorrencias in contador.items():
    arquivo_saida.write(f'{palavra}: {ocorrencias}\n')

# Fechar o arquivo de saída
arquivo_saida.close()