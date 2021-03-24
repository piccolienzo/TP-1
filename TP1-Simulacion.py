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
    plt.xlabel('Tamaño de muestra')
    plt.ylabel('Valor')
    plt.show()





MIN = 0
MAX = 36
SIZE = 100
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
"""
1. La ruleta va desde el 0 al 36 inclusive 

"""