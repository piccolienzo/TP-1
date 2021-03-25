import random
import collections
import numpy as np 
from scipy import stats 
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches



def getRandomInt():
    number = random.randint(MIN,MAX)
    return number

def getRandomIntList():
    randomList = []
    for x in range(MIN,SIZE):
        randomList.append(getRandomInt())
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
    plt.barh(PROM,width=(len(mediaList)), height=0.1, color="orange")
    blue_patch = mpatches.Patch(color='blue', label='Promedio de la muestra')
    plt.legend(handles=[blue_patch])
    plt.xlabel('Tirada')
    plt.ylabel('Valor de la media')
    plt.savefig("MEDIA_"+str(SIZE)+"_TIRADAS"+str(EXT))

def graficarMediana():
    plt.figure(figsize=(18,10))
    plt.plot(medianaList) 
    plt.title("Mediana a lo largo de "+str(SIZE)+" tiradas")
    blue_patch = mpatches.Patch(color='red', label='Valor de la mediana en los distintos puntos')
    plt.legend(handles=[blue_patch])
    plt.xlabel('Tirada')
    plt.ylabel('Valor de la mediana')
    plt.savefig("MEDIANA_"+str(SIZE)+"_TIRADAS"+str(EXT))
    

def graficarModa():
    numeros = []
    cantidades = []
    plt.figure(figsize=(18,10))
    for y in modaList:
        numeros.append(y[0][0])
        cantidades.append(y[1][0])
    plt.bar(range(SIZE),numeros) 
    
    plt.yticks(range(0,MAX),range(0,MAX))
    plt.ylim(min(numeros)-1,max(numeros)+1)
    plt.title("Moda a lo largo de "+str(SIZE)+ " tiradas")
    plt.xlabel('Tirada')
    plt.ylabel('Moda')
    plt.savefig("MODA_"+str(SIZE)+"_TIRADAS"+str(EXT))
    

def graficarDesviacion():
    s = 0

def graficarVarianza():
    d = 0

def graficarFrecuenciasAbsolutas(): #Bastones
    vals = [] #lista de frecuencias relativas
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
    
    plt.savefig("FRECUENCIAS_ABSOLTUAS_"+str(SIZE)+"_TIRADAS"+str(EXT))
    
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
    
    plt.savefig("FRECUENCIAS_RELATIVAS_"+str(SIZE)+"_TIRADAS"+str(EXT))


sizes = [100,500,1000]

for size in sizes:
    MIN = 0
    MAX = 36
    SIZE = size
    PROM =( MAX-MIN )/ 2
    EXT = ".png"
    #tendencias
    mediaList = []
    medianaList = []
    modaList = []
    #Dispersion 
    desviacionList = []
    varianzaList = []

    listaItems = []


    spectedNumber = getRandomInt()
    listaItems = getRandomIntList()
    countedList = countNumbers(listaItems)
    #graficarMedia()
    graficarMediana()
    #graficarModa()
    ##graficarFrecuenciasAbsolutas()
    #graficarFrecuenciasRelativas()


  
"""
1. La ruleta va desde el 0 al 36 inclusive 

"""