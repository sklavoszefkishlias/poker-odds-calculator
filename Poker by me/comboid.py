def getCombo(hand):
    #test change
    #getCombo returns the code of the card combinations the 5 cards of the hand object it receives
    #and it either returns and empty array when a same comboination code comparason dont need the
    # compisition of the cards(it just depends on he max of the sum of the cards example:Straights,
    #Flushes,High cards)
    #or it returns the frequency list which describes the sum of the card rank in each coresponding 
    #card position
    empty = [-1,-1,-1,-1,-1]
    returnList = []
    #Check if Straigt Flush
    #Checks if cards are the same suit
    sameSuitFlag=True
    for i in range(0,4):
        if hand[i].suit!=hand[i+1].suit:
            sameSuitFlag=False
    #Checks if cards are in range for stright
    rankList=[]
    for x in hand:
        rankList.append(int(x.rank))
    rankList.sort()
    min = rankList[0]
    min2 = rankList[1]
    max = rankList[4]
    if min == 1 and max > 5:
        min = min2
        max = 14
        
    if max - min == 4 and sameSuitFlag==True :
        if max==14:
            returnList = [10, empty]
            return returnList
        else:
            returnList = [9, empty]
            return returnList
    #Check 4 of a kind
    card=[hand[0].rank,hand[1].rank,hand[2].rank,hand[3].rank,hand[4].rank]
    frequency=[1,1,1,1,1]
    #Checks the frequency of duplicates
    #4s and 1s are 4 of a kind
    #3s and 2s are Full Fouses
    #2s and 2s are 2 pairs
    # 2 2 1 1 1  are 1 pair
    # 1 1 1 1 1 after not being straight flush ,flush or straight is high card 
    for x in range(0,5):
        for y in range(0,5):
            if hand[x].rank == hand[y].rank and x!=y:
                frequency[x] = frequency[x] + 1
    #Identifier works by making any type of card combo into a single identifiable set
    identifier=[0,0,0,0,0]
    for x in frequency:
        identifier[x-1]=1
    #4 of a kind
    if identifier == [1,0,0,1,0]:
        returnList = [8,frequency]
        return returnList
    #full house
    if identifier == [0,1,1,0,0]:
        returnList = [7 , frequency]
        return returnList
    #flush
    if sameSuitFlag==True:
        returnList = [6,empty]
        return returnList
    #Straight
    #Checks if there are duplicates in hand
    noDups=True
    for x in range (0,4):
        for y in range (x+1,5):
            if hand[x].rank == hand[y].rank:
                noDups=False
    if max - min == 4 and noDups==True:
        returnList = [5,empty]
        return returnList
    #three of a kind
    if identifier == [1,0,1,0,0]:
        returnList = [4, frequency]
        return returnList
    #two pair
    if identifier == [1,1,0,0,0]:
        counter = 0 
        for x in frequency:
            if x == 2:
                counter = counter + 1
        if counter > 2:
            returnList = [3, frequency]
            return returnList#code for 2 pair
        elif counter == 2:
            returnList = [2, frequency]
            return returnList#code for 1 pair
    if identifier == [1,0,0,0,0]:
        returnList= [1,empty]
        return returnList#code for high card

#get 5 out of the 52 cards and say what hand it makes
#getCombo returns an interger representing what type of combination the hand is
#Royal Flush = 10
#Straight Flush = 9
#4 of a kind = 8
#Full house = 7
#Flush = 6
#Straight = 5
#3 of a kind = 4
#2 pair = 3
#Pair = 2
#High card = 1


#Matches the code with the word
def getComboWord(cardComboCode):
    cardComboWord = ""
    match cardComboCode:
        case 10:
            cardComboWord = "Royal Flush"
        case 9:
            cardComboWord = "Straight Flush"
        case 8:
            cardComboWord = "4 of a Kind"
        case 7:
            cardComboWord = "Full House"
        case 6:
            cardComboWord = "Flush"
        case 5:
            cardComboWord = "Straight"
        case 4:
            cardComboWord = "3 of a Kind"
        case 3:
            cardComboWord = "2 Pair"
        case 2:
            cardComboWord = "1 Pair"
        case 1:
            cardComboWord = "High Card"
    return cardComboWord