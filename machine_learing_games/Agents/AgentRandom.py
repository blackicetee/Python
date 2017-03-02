from random import randint

def getRandomAction(possibleActionList):
    return possibleActionList[randint(0, (len(possibleActionList) - 1))]