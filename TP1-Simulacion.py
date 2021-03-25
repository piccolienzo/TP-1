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
    orange_patch = mpatches.Patch(color='orange', label='Promedio esperado')
    plt.legend(handles=[blue_patch,orange_patch])
    plt.xlabel('Tirada')
    plt.ylabel('Valor de la media')
    plt.savefig("MEDIA_"+str(SIZE)+"_TIRADAS"+str(EXT),bbox_inches='tight')
    plt.close()

def graficarMediana():
    plt.figure(figsize=(18,10))
    plt.plot(medianaList) 
    plt.title("Mediana a lo largo de "+str(SIZE)+" tiradas")
    plt.xlabel('Tirada')
    plt.ylabel('Valor de la mediana')
    plt.savefig("MEDIANA_"+str(SIZE)+"_TIRADAS"+str(EXT),bbox_inches='tight')
    plt.close()
    

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
    plt.xlabel('Tiradas')
    plt.ylabel('Moda')
    plt.savefig("MODA_"+str(SIZE)+"_TIRADAS"+str(EXT),bbox_inches='tight')
    plt.close()
    
    

def graficarDesviacion():
    plt.figure(figsize=(18,10))
    plt.plot(desviacionList) 
    plt.title("Desviación estándar a lo largo de "+str(SIZE)+ " tiradas")
    plt.xlabel('Tiradas')
    plt.ylabel('Valor de la desviación estándar')
    plt.savefig("DESVIACION_ESTANDAR_"+str(SIZE)+"_TIRADAS"+str(EXT),bbox_inches='tight')
    plt.close()

def graficarVarianza():
    plt.figure(figsize=(18,10))
    plt.plot(varianzaList) 
    plt.title("Varianza a lo largo de "+str(SIZE)+ " tiradas")
    plt.xlabel('Tiradas')
    plt.ylabel('Valor de la varianza')
    plt.savefig("VARIANZA_"+str(SIZE)+"_TIRADAS"+str(EXT),bbox_inches='tight')
    plt.close()

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
    
    plt.savefig("FRECUENCIAS_ABSOLUTAS_"+str(SIZE)+"_TIRADAS"+str(EXT),bbox_inches='tight')
    plt.close()
    
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
    
    plt.savefig("FRECUENCIAS_RELATIVAS_"+str(SIZE)+"_TIRADAS"+str(EXT),bbox_inches='tight')
    plt.close()


sizes = [100,500,1000]

for size in sizes:
    MIN = 0
    MAX = 36
    SIZE = size
    PROM =( MAX-MIN )/ 2
    EXT = ".svg"
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
    graficarMedia()
    graficarMediana()
    graficarModa()
    graficarFrecuenciasAbsolutas()
    graficarFrecuenciasRelativas()
    graficarVarianza()
    graficarDesviacion()
