#min() and max() doesnt work on hand.cards.rank but this works
def getMax(hand):
    max=int(hand[0].rank)
    for x in range(1,5):
        if int(hand[x].rank) > max:
            max = int(hand[x].rank)
    return max

def getMin(hand):
    min=int(hand[0].rank)
    for x in range(1,5):
        if int(hand[x].rank) < min:
            min = int(hand[x].rank)
    return min

#Code is the getComboCode output and validCode is the number of the index
# we need to extract from frequency 
def getValidCardIndex(frequency,code):
    validCode = 0
    if code == 8:
        validCode = 4
    elif code == 7 or code == 4:
        validCode = 3
    elif code == 2:
        validCode = 2
    
    if code == 8 or code == 7 or code == 4 or code == 2:

        for x in range(0,5):
            if frequency[x] == validCode:
                return x

#getTwoPairRanks checks the frequency list for the location of the pairs and returns a list
# with the ranks of the pairs example: [2,2,1,1]             
def getTwoPairRanks(hand):
    twoPairValid= []
    for x in range(0,5):
        if hand.comboFrequencyList[1][x]==2:
            twoPairValid.append(int(hand.cards[x].rank))
    return twoPairValid

def makeAceBeGreat(hand):
    if getMin(hand.cards)== 1 and getMax(hand.cards) == 5 and (hand.comboFrequencyList[0]==10 or hand.comboFrequencyList[0]==9 or hand.comboFrequencyList[0]==5):
        return 0
    else:
        return 1

#Recieves 2 hands objects
#It first checks for different card combination (easy ruling)
#if its the same then checks for the biggest card to determine
def getWinner(originalHand1,originalHand2):


    hand1 = originalHand1
    hand2 = originalHand2
    comboCode1=hand1.comboFrequencyList[0]
    frequency1=hand1.comboFrequencyList[1]
    comboCode2=hand2.comboFrequencyList[0]
    frequency2=hand2.comboFrequencyList[1]
    
    if makeAceBeGreat(hand1):
        for x in hand1.cards:
            if x.rank =="1":
                x.rank = "14"
    if makeAceBeGreat(hand2):
        for x in hand2.cards:
            if x.rank =="1":
                x.rank = "14"


    '''for x in range(0,5):
        print(hand1.cards[x].rank)
    for x in range(0,5):
        print(hand2.cards[x].rank)'''

    if comboCode1>comboCode2:
        return 1
    elif comboCode2>comboCode1:
        return 2
    elif comboCode1 == comboCode2:
        if comboCode1 == 10 or comboCode1 ==  9 or comboCode1 == 6 or comboCode1 == 5 or comboCode1 ==1:
            max1=getMax(hand1.cards)
            max2=getMax(hand2.cards)
            #print(max1 , max2)
            if max1>max2:
                return 1
            elif max1<max2:
                return 2
            else:
                return 0
        elif comboCode1 == 8 or comboCode1 == 7 or comboCode1 == 4 or comboCode1 == 2:
            validCardIndex1=getValidCardIndex(frequency1,comboCode1)
            validCardIndex2=getValidCardIndex(frequency2,comboCode2)
            if hand1.cards[validCardIndex1].rank > hand2.cards[validCardIndex2].rank:
                return 1
            elif hand1.cards[validCardIndex1].rank < hand2.cards[validCardIndex2].rank:
                return 2
            else:
                return 0
        #When two 2 pair hands are compaired to get the winnner you compair the bigger pair on
        # the first hand with the bigger pair of the second hand
        #if there are the same which is possible because the there are 4 times the same rank
        # the secondary(smaller) pairs of the 2 hands get compaired
        # if again they are the same then its a draw
        elif comboCode1 == 3:
            twoPairRanks=[]
            twoPairRanks2=[]
            twoPairRanks=getTwoPairRanks(hand1)
            twoPairRanks2=getTwoPairRanks(hand2)
            if max(twoPairRanks) > max(twoPairRanks2):
                return 1
            elif max(twoPairRanks) < max(twoPairRanks2):
                return 2
            elif max(twoPairRanks)== max(twoPairRanks2):
                if min(twoPairRanks) > min(twoPairRanks2):
                    return 1
                elif min(twoPairRanks) < min(twoPairRanks2):
                    return 2
                elif min(twoPairRanks)==min(twoPairRanks2):
                    return 0 
