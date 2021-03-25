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
    plt.figure(figsize=(18,10))
    plt.plot(mediaList) 
    plt.title("Media a lo largo de "+str(SIZE)+ " tiradas")
    blue_patch = mpatches.Patch(color='blue', label='Promedio de la muestra')
    plt.legend(handles=[blue_patch])
    plt.xlabel('Tirada')
    plt.ylabel('Valor de la media')
    plt.savefig("MEDIA_"+str(SIZE)+"_TIRADAS.svg")

def graficarMediana():
    plt.figure(figsize=(18,10))
    plt.plot(medianaList) 
    plt.title("Mediana a lo largo de "+str(SIZE)+" tiradas")
    blue_patch = mpatches.Patch(color='red', label='Valor de la mediana en los distintos puntos')
    plt.legend(handles=[blue_patch])
    plt.xlabel('Tirada')
    plt.ylabel('Valor de la mediana')
    plt.savefig("MEDIANA_"+str(SIZE)+"_TIRADAS.svg")
    

def graficarModa():
    numeros = []
    cantidades = []
    plt.figure(figsize=(18,10))
    for y in modaList:
        numeros.append(y[0][0])
        cantidades.append(y[1][0])
    plt.bar(range(SIZE),numeros,edgecolor="black") 
    plt.xticks(range(SIZE),range(SIZE))
    plt.ylim(min(numeros)-2,max(numeros)+1)
    plt.title("Moda a lo largo de "+str(SIZE)+ " tiradas")
    plt.xlabel('Tirada')
    plt.ylabel('Moda')
    plt.savefig("MODA_"+str(SIZE)+"_TIRADAS.svg")
    

def graficarDesviacion():
    s = 0

def graficarVarianza():
    d = 0

def graficarFrecuenciasAbsolutas(): #Bastones
    vals = [] #lista de conteos
    keys = [] #lista de numeros
    for key in countedList.keys():
        keys.append(key)
    for value in countedList.values():
        vals.append(value)
    plt.figure(figsize=(18,10))
    
    for index in range(len(vals)):
        plt.bar(keys[index],vals[index],align="center",width=0.1)
    plt.xticks(keys)
    plt.yticks(vals)
    
    plt.title("Frecuencias absolutas para "+str(SIZE)+ " tiradas")
    plt.xlabel("Números")
    plt.ylabel("Frecuencia")
    
    plt.savefig("FRECUENCIAS_ABSOLTUAS_"+str(SIZE)+"_TIRADAS.svg")
    
def graficarFrecuenciasRelativas():
    vals = [] #lista de conteos
    keys = [] #lista de numeros
    for key in countedList.keys():
        keys.append(key)
    for value in countedList.values():
        vals.append(value/SIZE)
    plt.figure(figsize=(18,10))
    
    for index in range(len(vals)):
        plt.bar(keys[index],vals[index],align="center",width=0.1)
    plt.xticks(keys)
    plt.yticks(vals)
    
    plt.title("Frecuencias relativas para "+str(SIZE)+ " tiradas")
    plt.xlabel("Números")
    plt.ylabel("Frecuencia")
    
    plt.savefig("FRECUENCIAS_RELATIVAS_"+str(SIZE)+"_TIRADAS.svg")


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

listaItems = []


spectedNumber = getRandomInt(MIN,MAX)
listaItems = getRandomIntList(SIZE)
print(listaItems)
countedList = countNumbers(listaItems)
"""print("media")
print(mediaList)
print("mediana")
print(medianaList)
print("desviacion estandar")
print(desviacionList)
print("varianza")
print(varianzaList)
print("moda")
print(modaList)"""


#graficarMedia()
#graficarMediana()
#graficarModa()
#graficarFrecuenciasAbsolutas()
graficarFrecuenciasRelativas()


  
"""
1. La ruleta va desde el 0 al 36 inclusive 

"""