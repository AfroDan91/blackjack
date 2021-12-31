import random
import time as t

spades = ["s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "sj", "sq", "sk"]
clubs = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "cj", "cq", "ck"]
hearts = ["h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "hj", "hq", "hk"]
diamonds = ["d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "dj", "dq", "dk"]
deck = ["s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "sj", "sq", "sk", "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "cj", "cq", "ck","h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "hj", "hq", "hk","d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "dj", "dq", "dk"]
burned = []
playersCards = []
pcCards = []
playerTotal = 0
pcTotal = 0
playerPlaying = True
pcPlaying = True
playerBusted = False
pcBusted = False
wins = 0
losses = 0
gamesPlayed = 0
playAnother = True
playerDone = False

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
    global playAnother
    if response.lower() == "yes" or response.lower() == "y":
        playAnother = True
    else:
        playAnother = False


def resetGame():
    global deck
    global burned
    global playersCards
    global pcCards
    global playerTotal
    global pcTotal
    global playerPlaying
    global pcPlaying
    global playerBusted
    global pcBusted
    deck = ["s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "sj", "sq", "sk", "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "cj", "cq", "ck","h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "hj", "hq", "hk","d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "dj", "dq", "dk"]
    burned = []
    playersCards = []
    pcCards = []
    playerTotal = 0
    pcTotal = 0
    playerPlaying = True
    pcPlaying = True
    playerBusted = False
    pcBusted = False


#game Starts
while playAnother == True:
    
    for card in range(2):                       #draw 2 cards for player              
        chosenCard = drawCard(playersCards)     #Pick a card and return the card and its value
        playerTotal += chosenCard[1]            #Add the value to the player's total hand value

    playersHand = ', '.join(str(card) for card in playersCards)     #turns the list of cards into a string
    print(f"You have drawn {playersHand}")                          #Prints the string of cards chosen
    print(f"Your hand value is {playerTotal}")                      #Displays hand value

    #draw and remove 2 cards for pc
    for card in range(2):                               #Draw 2 cards for the dealer
        chosenCard = drawCard(pcCards)                  #Pick a card and return the card and its value
        pcTotal += chosenCard[1]                        #Add the value to the dealer's total hand value
    pcHand = ', '.join(str(card) for card in pcCards)   #turns the list of cards into a string


    # prompt payer for action stick or twist
    while playerPlaying == True:
        action = input("Would you like to (s)tick or (t)wist? ")

        if action.lower() == "t" or action.lower() == "twist" or action.lower() == "hit":
            chosenCard = drawCard(playersCards)
            playerTotal += chosenCard[1]
            print(f"You have drawn {chosenCard[0]}")
            print(f"Your hand value is {playerTotal}")            
        else:
            playerPlaying = False


        if playerTotal > 21:
            playerPlaying = False
            playerBusted = True
            print(f"Your hand value is {playerTotal}. BUSTED")
        elif playerTotal == 21:
            print(f"Your hand value is {playerTotal}!")
            playerPlaying = False


    t.sleep(2)
    print("\nIts now the dealers turn")
    t.sleep(1)
    print(f"\nThe dealer drew {pcHand}")
    print(f"Their hand value is {pcTotal}")
    t.sleep(3)

    while pcPlaying == True:
        if pcTotal >= 17:
            pcPlaying = False
            if pcTotal > 21:
                pcBusted = True
                print("The Dealer BUSTED!")
        else:        
            print("\nThe Dealer will take a card")
            t.sleep(1)
            chosenCard = drawCard(pcCards)
            pcTotal += chosenCard[1] 
            print(f"The Dealer drew the {chosenCard[0]}")
            t.sleep(1)
            print(f"The Dealer's hand value is {pcTotal}")
            t.sleep(3)


    while pcPlaying == False and playerPlaying == False:
        if playerTotal > pcTotal and playerTotal < 22:
            wins += 1
            gamesPlayed += 1
            print(f"You win this had! Well done. That makes {wins} wins and {losses} losses.")
            resetGame()
            playAgain()


        elif pcBusted == True and playerBusted == False:
            wins += 1
            gamesPlayed += 1
            print(f"You win this had! Well done. That makes {wins} wins and {losses} losses.")
            resetGame()
            playAgain()
 
        
        elif playerTotal == pcTotal and playerBusted == False:
            gamesPlayed += 1
            print(f"Both the you and the Dealer have {playerTotal}. The hand is a tie.")
            resetGame()
            playAgain()

        
        elif pcBusted == True and playerBusted == True or pcTotal > playerTotal and pcTotal < 22:
            losses += 1
            gamesPlayed += 1
            print(f"The house wins this time, Sorry. That is {wins} wins and {losses} losses.")
            resetGame()
            playAgain()
            deck = ["s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "sj", "sq", "sk", "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "cj", "cq", "ck","h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "hj", "hq", "hk","d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "dj", "dq", "dk"]


        elif playerBusted == True and pcBusted == False:
            losses += 1
            gamesPlayed += 1
            print(f"The house wins this time, Sorry. That is {wins} wins and {losses} losses.")
            resetGame()
            playAgain()
 
        

        

print("Thanks for playing Daniel's Blackjack")
print("\n\nBreakdown:")
print(f"You played {gamesPlayed} time and won {wins} hands, lost {losses} hands and tied {gamesPlayed - (wins + losses)} hands. ")
if wins > losses:
    print("You won more than you lost! Well done. Now you are ready to do it for real")
else:
    print("Looks like you need a little more practice.")

print("See you again soon.")


    


#evaluate pc cards

#pc takes acton 

#find winner
