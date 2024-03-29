#Projeto Previsão de vendas(Ciência de dados)

#1- Entendendo o desafio

#2- Entendimento da Area/Empresa

#3- Extração/Obtenção de Dados
#Importar a base de dados

from statistics import LinearRegression
import pandas as pd
tabela = pd.read_csv("advertising.csv")
print(tabela)

#4- Ajuste de Dados(Tratamento/limpeza)

# Instalar
#pip install matplotlib -> Gráficos
#pip install seaborn -> Gráficos
#pip install scikit-learn -> inteligência artificial

#5- Análise exploratória
#Vamos tentar visualizar como as informações de cada item estão distribuidas
#Vamos ver a correlação de cada um dos itens

import seaborn as sns
import matplotlib.pyplot as plt

print(tabela.corr())

# Criar o gráfico
sns.heatmap(tabela.corr(), cmap="wistia", annot=True)

# Exibir o gráfico
plt.show()

# Com isso, podemos partir para a preparação dos dados para treinarmos o Modelo de Machine Learning
#separando dos dados de treino e dados de teste
#Y -> Quem você quer prever
#X -> É o resto todo da base de dados(quem você vai usar para fazer a previsão)

x= tabela[["TV", "Radio", "Jornal"]] # -> sempre que tiver mais de um dado, coloca-se 2 colchetes.
y= tabela["Vendas"]

from sklearn.model_selection import train_test_split

x_treino, x_teste, y_treino, y_teste = train_test_split(x,y) #separar dados de treino e teste(80,20), para treinar a A.I.

#Temos um problema de regressão = vamos escolher os modelos que vamos usar.

#Regressão Linear

from sklearn.linear_model import LinearRegression

modelo_regressaoLinear = LinearRegression() #cria A.I.
modelo_regressaoLinear.fit(x_treino, y_treino) #treina A.I.

#RandomForest(Arvore de Decisão)

from sklearn.ensemble import RandomForestRegressor


modelo_arvoredecisao = RandomForestRegressor() #cria A.I.
modelo_arvoredecisao.fit(x_treino, y_treino) #treina A.I.

#Fazer previsão nos testes

previsao_regressaolinear = modelo_regressaoLinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)

#calcula o R².

from sklearn.metrics import r2_score

print(r2_score(y_teste,previsao_regressaolinear)) #0.90
print(r2_score(y_teste,previsao_arvoredecisao)) #0.96

#Melhor modelo = Arvore de decisão

#como fazer uma nova previsão?

novos = pd.read_csv("novos.csv")
print(novos)

print(modelo_arvoredecisao.predict(novos))


#6- Modelagem + Algoritimos(aqui entra a inteligência artificial, se for o caso)


#7- Interpretação de Resultados
