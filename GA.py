import numpy as np
import matplotlib.pyplot as plt
NumeroDeGeracoes = 1000
NumeroDeGenes = 10
TamanhoDaPopulacao = 30
TamanhoDaElite = 5
Populacao = np.zeros((TamanhoDaPopulacao, NumeroDeGenes + 1))
# Fitness ficara armazenado na populacao, em NumeroDeGenes + 1
def InicializaPopulacao():
    global Populacao
    Populacao = np.random.rand(TamanhoDaPopulacao, NumeroDeGenes + 1)
    Populacao[:, NumeroDeGenes] = np.zeros(TamanhoDaPopulacao) 
    #print("Populacao inicial: \n",Populacao)
    return
def AvaliaPopulacao():
    global Populacao
    for p in range(TamanhoDaPopulacao):
        Populacao[p, NumeroDeGenes] = np.sum(Populacao[p, 0:NumeroDeGenes])
    #print("Populacao avaliada: \n",Populacao)    
    return
def SelecionaMelhores():
    Bolha = np.zeros((TamanhoDaPopulacao, NumeroDeGenes + 1))
    global Populacao 
    Bolha[:, :] = Populacao[np.argsort(Populacao[:, NumeroDeGenes]), :]
    Populacao = Bolha
    #print("Populacao Selecionada: \n", Populacao)
    return
def AtualizaPopulacao():
    global Populacao
    Populacao[TamanhoDaElite:TamanhoDaPopulacao, :] = np.random.rand(TamanhoDaPopulacao - TamanhoDaElite, NumeroDeGenes + 1)
    Populacao[TamanhoDaElite:TamanhoDaPopulacao, NumeroDeGenes] = np.zeros(TamanhoDaPopulacao - TamanhoDaElite) 
    #print("Populacao Atualizada: \n", Populacao)
    return
InicializaPopulacao()
Saida = np.zeros(NumeroDeGeracoes)
for t in range(NumeroDeGeracoes):
  AvaliaPopulacao()
  SelecionaMelhores()
  AtualizaPopulacao()
  Saida[t] = Populacao[0, NumeroDeGenes]
#Eixo = i for i in range(NumeroDeGeracoes)
plt.plot(Saida)
plt.title('Fitness/Geração')
plt.xlabel('Geração')
plt.ylabel('Fitness')
plt.show()