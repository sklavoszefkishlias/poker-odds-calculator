import comboid as module1
class Card :

    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank

    def getCard(self):
        x=self.rank
        if self.rank =="11":
            x = "J"
        elif self.rank =="12":
            x = "Q" 
        elif self.rank == "13":
            x = "K"
        elif self.rank == "14":
            x = "A"
        return x + self.suit

class Player :

    def __init__(self,card1,card2):
        self.card1=card1
        self.card2=card2

    def getHand(self):
        return self.card1.getCard(),self.card2.getCard()

#For easier combination evaluation and compairng 5 card combinations
class Hand :
    def __init__(self,card1,card2,card3,card4,card5):
        self.cards = [card1,card2,card3,card4,card5]
    def getCombination(self):
        self.comboFrequencyList=module1.getCombo(self.cards)
    def getCards(self):
        array = []
        for x in self.cards:
            array.append(x.rank + x.suit)
        return array


class Data:
    def __init__(self,num,pList):
        self.num = num
        self.playerList = pList
        self.array=[]


    def collectData(self,data):
        self.array.append(data)
    
    def readyData(self):
        self.ready = f"Players:\n"
        for x in range(0,self.num):
            self.ready += f"Player {x+1}: {self.playerList[x].card1.getCard()}, {self.playerList[x].card1.getCard()}\n"
        for x in range(0,3):
            for y in range(0,len(self.array[x])-1) :  
                self.ready += f"Player {y+1} Odds:{round(self.array[x][y],2)}%\n"
            self.ready += f"Draw Odds:{round(self.array[x][len(self.array[x])-1],2)}%\n"



    def getReady(self):
        return self.ready
    
    def getData(self):
        return self.array
    

