from itertools import combinations
import module2
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




def getEquity(pList,table,deck,gameStateDraw):
    '''
    in each gamestate the amount of random card gets smaller
    in preflop we get 5 random  cards
    then 2 then 1 and then 0
    we need to ghet every single combination of these random cards
    for each unique comvination of the random cards we need to combine 
    them with the known cards them being the player cards and 
    according to the gamestate the known common cards
    then out of the 21 5 card combination of hte 7card set
    for each player we must get the best of those and then compare
    the p1 and p2 best combo
    then we number the p1 wins the p2 wins and the ties
    out of those statictcics we will produce the win loose precentages
    '''
    array = list(combinations(deck , gameStateDraw))
    winList = []
    for x in range(0,len(pList)):
        winList.append(0)
    draws = 0
    total = 0
    result = 0
    winList = []
    for x in range(0,len(pList)):
        winList.append(0)
    
    #give credits to https://stackoverflow.com/questions/65889095/how-to-get-
    # itertools-combinations-as-list-of-lists-without-for-loop
    array1 = []
    for i in array:
        array1.append(list(i))
    for x in array1:
        tableMut = table.copy()
        tableMut.extend(x)
        pListSeven = []
        Best = [] 
        for x in range(0,len(pList)):
            pSeven = [pList[x].card1, pList[x].card2]
            pSeven.extend(tableMut)
            pListSeven.append(pSeven)
            Best.append(getBestSeven(pListSeven[x]))
            pSeven.clear()

        tableMut.clear()
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