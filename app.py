import random

spades = ["s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "sj", "sq", "sk"]
clubs = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "cj", "cq", "ck"]
hearts = ["h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "hj", "hq", "hk"]
diamonds = ["d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "dj", "dq", "dk"]
deck =["s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "sj", "sq", "sk", "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "cj", "cq", "ck","h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "hj", "hq", "hk","d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "dj", "dq", "dk"]
burned = []
playersCards = []
pcCards = []
playerTotal = 0
pcTotal = 0
stick = False
playerBusted = False
pcBusted = False
wins = 0
losses = 0
gamesPlayed = 0
playAnother = True

def drawCard(userCards):                        #to draw a card from the deck
    cardIndex = random.randint(1, len(deck))    #chose a random number from the number of cards remaining in the deck
    chosenCard = deck.pop(cardIndex-1)          #use that number to find the corresponding card
    burned.append(chosenCard)                   #add that card to the burned cards pile
    userCards.append(chosenCard)                #add that card to the users card list
    cardValue = readCard(chosenCard)            #figure out the numerical value of the card
    return [chosenCard, cardValue]              #return the card and card value


def readCard(card):                                 #to read a card
    if "j" in card or "q" in card or "k" in card:   #if the card has a face tag 
        return 10                                   #return its value as 10
    else:                                           #if not
        return int(card[1:])                        #return the number of the card


def playAgain():
    response = input("Would you like to play another hand? (y)es or (n)o ")
    if response.lower() == "yes" or response.lower() == "y":
        playAnother == True
    else:
        playAnother == False


def resetDeck():
    for card in burned:
        deck.append(card)


#game Starts
while playAnother == True:
    #draw 2 cards for player
    for card in range(2):                       
        chosenCard = drawCard(playersCards)
        playerTotal += chosenCard[1]

    #Tell the player the cards they have drawn
    playersHand = ', '.join(str(card) for card in playersCards) #turns the list of cards into a string
    print(f"You have drawn {playersHand}")
    print(f"Your hand value is {playerTotal}")

    #draw and remove 2 cards for pc
    for card in range(2):                  
        chosenCard = drawCard(pcCards)
        pcTotal += chosenCard[1]
    pcHand = ', '.join(str(card) for card in pcCards) #turns the list of cards into a string
    # def requestresponse():
    #     action = input("Would you like to (s)tick or (t)wist? ")
    #     if action.lower() == "s" or action.lower() == "stick":
    #         chosenCard = drawCard(playersCards)
    #     return chosenCard


    # prompt payer for action stick twist
    while playerTotal != 21 and playerBusted == False and stick == False:
        action = input("Would you like to (s)tick or (t)wist? ")

        if action.lower() == "t" or action.lower() == "twist" or action.lower() == "hit":
            chosenCard = drawCard(playersCards)
            playerTotal += chosenCard[1]
        else:
            stick = True

        print(f"You have drawn {chosenCard[0]}")
        print(f"Your hand value is {playerTotal}")

        if playerTotal > 21:
            playerBusted = True
            print(f"Your hand value is {playerTotal}. BUSTED")
        elif playerTotal == 21:
            print(f"Your hand value is {playerTotal}!")

    print("Its now the dealers turn")
    print(f"The dealer drew {pcHand}")
    print(f"Their hand value is {pcTotal}")

    while pcTotal < 16 and pcBusted == False:
        print("The Dealer will take a card")
        chosenCard = drawCard(pcCards)
        pcTotal += chosenCard[1] 
        print(f"The Dealer drew the {chosenCard[0]}")
        print(f"The Dealer's hand value is {pcTotal}")
        if pcTotal > 21:
            pcBusted = True


    if playerTotal > pcTotal and playerTotal < 22:
        wins += 1
        gamesPlayed += 1
        print(f"You win this had! Well done. That makes {wins} wins and {losses} losses.")
        resetDeck()
        playAgain()
    elif playerTotal == pcTotal and playerBusted == False:
        gamesPlayed += 1
        print(f"Both the you and the Dealer have {playerTotal}. The hand is a tie.")
        resetDeck()
        playAgain()
    elif pcBusted == True and playerBusted == True or pcTotal > playerTotal and pcTotal < 22:
        losses += 1
        gamesPlayed += 1
        print(f"The house wins this time, Sorry. That is {wins} wins and {losses} losses.")
        resetDeck()
        playAgain()

print("Thanks for playing Daniel's Blackjack")
print("Breakdown:")
print(f"You played {gamesPlayed} games and won {wins} hands, lost {losses} hands and tied {gamesPlayed - (wins + losses)} ")
if wins > losses:
    print("You won more than you lost! Well done. Now you are ready to do it for real")
else:
    print("Looks like you need a little more practice.")

print("See you again soon.")


    


#evaluate pc cards

#pc takes acton 

#find winner
