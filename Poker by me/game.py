import random
import equitymodule
import comboid as module1
import module4
from pokerclasses import Hand,Card,Player, Data


def getOdds(num):
    #Make and shuffle deck
    Suits = ["♦","♠","♥","♣"]
    Ranks = ["1","2","3","4","5","6","7","8","9","10","11","12","13"]
    Deck=[]
    numberOfPlayers = num

    oddsList = [[] for _ in range(4)]
    
    for x in Ranks:
        for y in Suits:
            Deck.append(Card(y,x))
    random.shuffle(Deck)

    playerList = []
    for x in range(0,numberOfPlayers):
        playerList.append(Player(Deck.pop(0),Deck.pop(0)))


    data = Data(numberOfPlayers,playerList)




    table = []
    gameStateDraw = 5

    stats = module4.monteCarlo(playerList,Deck)
    data.collectData(stats)

    oddsList[0].append(str(round(stats[len(stats)-1],2)))
    for x in range(0,len(stats)-1) :  
        oddsList[0].append(str(round(stats[x],2)))

    #Flop
    table.append(Deck.pop(0))
    table.append(Deck.pop(0))
    table.append(Deck.pop(0))

    gameStateDraw = 2

    stats = equitymodule.getEquity(playerList,table,Deck,gameStateDraw)
    data.collectData(stats)

    oddsList[1].append(str(round(stats[len(stats)-1],2)))
    for x in range(0,len(stats)-1) :  
        oddsList[1].append(str(round(stats[x],2)))
        

    #Turn
    table.append(Deck.pop(0))

    gameStateDraw = 1

    stats = equitymodule.getEquity(playerList,table,Deck,gameStateDraw)
    data.collectData(stats)

    oddsList[2].append(str(round(stats[len(stats)-1],2)))
    for x in range(0,len(stats)-1) :  
        oddsList[2].append(str(round(stats[x],2)))

    oddsList[2][0] = str(round(stats[len(stats)-1],2))
    
    #River
    table.append(Deck.pop(0))

    gameStateDraw = 0

    stats = equitymodule.getEquity(playerList,table,Deck,gameStateDraw)
    data.collectData(stats)
    
    oddsList[3].append(str(round(stats[len(stats)-1],2)))
    for x in range(0,len(stats)-1) :  
        oddsList[3].append(str(round(stats[x],2)))


    #100-0 or 50-50

    data.readyData()

    with open("data.txt", "a") as f:
        f.write("START OF RECORD\n")
        f.write(data.getReady())
        f.write("END OF RECORD\n\n")
    
    cardList = [[] for _ in range(numberOfPlayers + 1)]
    cardList[0] = [table[0].getCard(),table[1].getCard(),table[2].getCard(),table[3].getCard(),table[4].getCard()]
    for x in range(0,numberOfPlayers):
        cardList[x+1] = playerList[x].getHand()

    for row in oddsList:
        for i in range(len(row)):
            row[i] = f"{row[i]}%"

    return cardList, oddsList

