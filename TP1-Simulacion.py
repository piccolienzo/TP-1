import random
import collections


def getRandomInt(min,max):

    number = random.randint(min,max)
    return number

def getRandomIntList(size):
    randomList = []
    for x in range(size):
        randomList.append(getRandomInt(0,36))   
           
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


MIN = 0
MAX = 36
SIZE = 1369

spectedNumber = getRandomInt(MIN,MAX)
li = getRandomIntList(SIZE)
print(li)
countedList = countNumbers(li)
print(countedList)
print("valor esperado " + str(spectedNumber) + " fue encontrado " + str(countedList[spectedNumber]) + " veces")
print("frecuencia relativa esperada: " + str(1/MAX) + " frecuencia relativa obtenida " + str(countedList[spectedNumber]/SIZE))

"""
1. La ruleta va desde el 0 al 36 inclusive

"""