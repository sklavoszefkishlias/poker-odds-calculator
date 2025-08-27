import random
import module2
from itertools import combinations
import pokerclasses




def getBestSeven(sevenCards):
    hand = []
    array = combinations(sevenCards,5)
    array1 = []
    for i in array:
        array1.append(list(i))
    for x in array1:
        hand.append(pokerclasses.Hand(x[0],x[1],x[2],x[3],x[4]))
    for x in hand:
        x.getCombination()
    while True:
        result = module2.getWinner(hand[0],hand[1])
        if result == 1 or result == 0:
            hand.pop(1)
        elif result == 2:
            hand.pop(0)
        if len(hand) == 1:
            break
    return hand[0]





def monteCarlo(pList,deck):
    winList = []
    for x in range(0,len(pList)):
        winList.append(0)
    draws = 0
    total = 0
    result = 0

    monteCarloArray= []
    for x in range(0,10000):
        random.shuffle(deck)
        array= [deck[0],deck[1],deck[2],deck[3],deck[4]]
        monteCarloArray.append(array)
    for x in monteCarloArray:
        pListSeven=[]
        Best = []
        for y in range(0,len(pList)):
            pSeven = [pList[y].card1, pList[y].card2]
            pSeven.extend(x)
            pListSeven.append(pSeven)
            Best.append(getBestSeven(pListSeven[y]))
            pSeven.clear()
        bestIndex = []
        for x in range(0,len(pList)):
            bestIndex.append(x)
        x = 0
        drawFlag = False
        while True:
            drawFlag = False
            result = module2.getWinner(Best[x],Best[x+1])
            if result == 1:
                Best.pop(x+1)
                bestIndex.pop(x+1)
            elif result == 2:
                Best.pop(x)
                bestIndex.pop(x)
            elif result ==0:
                Best.pop(x+1)
                bestIndex.pop(x+1)
                drawFlag = True
            if len(Best) == 1:
                break
        if drawFlag == True:
            draws +=1
        else:
            for x in range(0,len(pList)):
                if bestIndex[0] == x:
                    winList[x] +=1
        total +=1
    probList=[]
    for x in winList:
        probList.append(x/total*100)
    
    probList.append(draws/total*100)
    return probList