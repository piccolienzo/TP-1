import random
import collections
import numpy as np 
from scipy import stats 
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches



def getRandomInt(min,max):

    number = random.randint(min,max)
    return number

def getRandomIntList(size):
    randomList = []
    for x in range(size):
        randomList.append(getRandomInt(0,36))
        proccessData(randomList)   
           
    return randomList

def countNumbers(rList):
    countList = {}
    for item in rList:
        if item in countList:
           
            countList[item] +=1
        else:
            countList[item]=1
    """countList = collections.OrderedDict(sorted(countList.items()))"""
    return countList

def proccessData(itemList):
        
    mediaList.append(np.mean(itemList))
    medianaList.append(np.median(itemList))
    desviacionList.append(np.std(itemList))
    varianzaList.append(np.var(itemList))
    modaList.append(stats.mode(itemList))


def graficarMedia():
    plt.plot(mediaList) 
    plt.title("Evolución de la Media")
    blue_patch = mpatches.Patch(color='blue', label='Promedio de la muestra')
    plt.legend(handles=[blue_patch])
    plt.xlabel('Tirada')
    plt.ylabel('Valor de la media')
    plt.show()

def graficarMediana():
    plt.plot(medianaList) 
    plt.title("Evolución de la Mediana")
    blue_patch = mpatches.Patch(color='red', label='Valor de la mediana en los distintos puntos')
    plt.legend(handles=[blue_patch])
    plt.xlabel('Tirada')
    plt.ylabel('Valor de la mediana')
    plt.show()

def graficarModa():
    numeros = []
    cantidades = []
    
    for y in modaList:
        numeros.append(y[0][0])
        cantidades.append(y[1][0])
    plt.bar(range(SIZE),numeros,edgecolor="black") 
    plt.xticks(range(SIZE),range(SIZE))
    plt.ylim(min(numeros)-2,max(numeros)+1)
    plt.title("Moda a lo largo de las corridas")
    plt.xlabel('Tirada')
    plt.ylabel('Moda')
    plt.show()

def graficarDesviacion():
    s = 0

def graficarVarianza():
    d = 0



MIN = 0
MAX = 36
SIZE = 10
#tendencias
mediaList = []
medianaList = []
modaList = []
#Dispersion 
desviacionList = []
varianzaList = []



spectedNumber = getRandomInt(MIN,MAX)
li = getRandomIntList(SIZE)
print(li)
countedList = countNumbers(li)
print("media")
print(mediaList)
print("mediana")
print(medianaList)
print("desviacion estandar")
print(desviacionList)
print("varianza")
print(varianzaList)
print("moda")
print(modaList)


graficarMedia()
graficarMediana()
graficarModa()


  
"""
1. La ruleta va desde el 0 al 36 inclusive 

"""