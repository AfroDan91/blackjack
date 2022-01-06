import random
import time as t


class hand():
    def __init__(self):
        shoe = []
        self.cardList = []
        self.handList = []
        self.handValue = 0
        self.bustedStatus = False

    def addHandToHandList(self,handToReplace):
        
        self.handlist.append(self.cardList)

    def createShoe(self, numberOfDecks):
        standardDeck = ["♠1", "♠2", "♠3", "♠4", "♠5", "♠6", "♠7", "♠8", "♠9", "♠10", "♠j", "♠q", "♠k", "♣1", "♣2", "♣3", "♣4", "♣5", "♣6", "♣7", "♣8", "♣9", "♣10", "♣j", "♣q", "♣k","♥1", "♥2", "♥3", "♥4", "♥5", "♥6", "♥7", "♥8", "♥9", "♥10", "♥j", "♥q", "♥k","♦1", "♦2", "♦3", "♦4", "♦5", "♦6", "♦7", "♦8", "♦9", "♦10", "♦j", "♦q", "♦k"]
        shoe = []
        for i in range(numberOfDecks):
            shoe += standardDeck
        return shoe

    def bustCheck(self, handValue):
        if handValue > 21:
            return True
        else:
            return False


    def drawCard(self, shoe):                                                           
        chosenCard = shoe.pop(random.randint(0, len(shoe)-1))                            #choose a card from the shoe
        self.cardList.append(chosenCard)                                                #add the card to the list of cards in this hand

        if chosenCard[1:] == "j" or chosenCard[1:] == "q" or chosenCard[1:] == "k":     #If the chosen card is a face...
            self.handValue += 10                                                        #add 10 to the hand value
            self.bustedStatus = self.bustCheck(self.handValue)                          #check if the hand value is over 21. If it is, set bustedStatus to True

        elif chosenCard[1:] == "1":                                                     #If the chosen card is an ace...
            self.handValue += 11                                                        #add 11 to the hand value
            self.bustCheck(self.handValue)                                              #check if the hand value is over 21. If it is, set bustedStatus to True

            if self.bustedStatus == True:                                               #If bustedStatus is true...
                self.handValue -= 10                                                    #take 10 away from the hand value
                self.bustedStatus = self.bustCheck(self.handValue)                      #check if the hand value is over 21. If it is, set bustedStatus to True

        else:                                                                           #If the card is nether a face or an ace...
            self.handValue += int(chosenCard[1:])                                       #add its card value to the hand value
            self.bustedStatus = self.bustCheck(self.handValue)                          #check if the hand value is over 21. If it is, set bustedStatus to True



class Player(hand):
    def __init__(self):
        super().__init__()
        self.name = "Dan"
        self.handList = []

# class Dealer(hand):


#TESTING
player1 = Player()
player1.shoe = player1.createShoe(2)
player1.drawCard(player1.shoe)
player1.drawCard(player1.shoe)

print(f"player name = {player1.name}")
print(f"list of players hands = {player1.handList}")
print(f"list of cards in players hand = {player1.cardList}")
print(f"players hand value = {player1.handValue}")
print(f"the entire shoe = {player1.shoe}")
print(f"player busted status = {player1.bustedStatus}")