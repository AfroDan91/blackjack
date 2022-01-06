import random
import time as t

spades = ["s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "sj", "sq", "sk"]
clubs = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "cj", "cq", "ck"]
hearts = ["h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "hj", "hq", "hk"]
diamonds = ["d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "dj", "dq", "dk"]
deck = ["♠1", "♠2", "♠3", "♠4", "♠5", "♠6", "♠7", "♠8", "♠9", "♠10", "♠j", "♠q", "♠k", "♣1", "♣2", "♣3", "♣4", "♣5", "♣6", "♣7", "♣8", "♣9", "♣10", "♣j", "♣q", "♣k","♥1", "♥2", "♥3", "♥4", "♥5", "♥6", "♥7", "♥8", "♥9", "♥10", "♥j", "♥q", "♥k","♦1", "♦2", "♦3", "♦4", "♦5", "♦6", "♦7", "♦8", "♦9", "♦10", "♦j", "♦q", "♦k"]
burned = []
playersCards = []
playersCards2 = []
pcCards = []
playerTotal = 0
playerTotal2 = 0
playersHandsList = []
pcTotal = 0
playerPlaying = True
pcPlaying = True
playerBusted = False
playerBusted2 = False
pcBusted = False
wins = 0
losses = 0
gamesPlayed = 0
playAnother = True
playerDone = False

def drawCard(userCards):                        #to draw a card from the deck
    cardIndex = random.randint(0, len(deck))    #chose a random number from the number of cards remaining in the deck
    chosenCard = deck.pop(cardIndex)            #use that number to find the corresponding card
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
    response = input("Would you like to play another hand? (y)es or (n)o ")     #offer the option to play again 
    global playAnother                                                          #import the global bool playAnother
    if response.lower() == "yes" or response.lower() == "y":                    #if player wants to play another hand...
        playAnother = True                                                      #set playAnother to true
    else:                                                                       #if not
        playAnother = False                                                     #set playAnother to false


def resetGame():
    global deck             #   ┐
    global burned           #   |
    global playersCards     #   |
    global pcCards          #   |
    global playerTotal      #   | import global variables
    global pcTotal          #   |
    global playerPlaying    #   |
    global pcPlaying        #   |
    global playerBusted     #   |
    global pcBusted         #   ┘
    deck = ["♠1", "♠2", "♠3", "♠4", "♠5", "♠6", "♠7", "♠8", "♠9", "♠10", "♠j", "♠q", "♠k", "♣1", "♣2", "♣3", "♣4", "♣5", "♣6", "♣7", "♣8", "♣9", "♣10", "♣j", "♣q", "♣k","♥1", "♥2", "♥3", "♥4", "♥5", "♥6", "♥7", "♥8", "♥9", "♥10", "♥j", "♥q", "♥k","♦1", "♦2", "♦3", "♦4", "♦5", "♦6", "♦7", "♦8", "♦9", "♦10", "♦j", "♦q", "♦k"]
    burned = []             #   ┐
    playersCards = []       #   |
    playersCards2 = []      #   |
    pcCards = []            #   |
    playersHandsList = []   #   |
    playerTotal = 0         #   |
    playerTotal2 = 0        #   |reset the gamestate to default
    pcTotal = 0             #   |
    playerPlaying = True    #   |
    pcPlaying = True        #   |
    playerBusted = False    #   |
    playerBusted2 = False   #   |
    pcBusted = False        #   ┘


#game Starts
while playAnother == True:
    
################## INITIAL DRAW ####################

    for card in range(2):                       #draw 2 cards for player              
        chosenCard = drawCard(playersCards)     #Pick a card and return the card and its value
        playerTotal += chosenCard[1]            #Add the value to the player's total hand value

    playersHand = ', '.join(str(card) for card in playersCards)     #turns the list of cards into a string
    print(f"You have drawn {playersHand}")                          #Prints the string of cards chosen
    print(f"Your hand value is {playerTotal}")                      #Displays hand value

    if playersCards[0][1:] == playersCards[1][1:]:
        splitq = input("Both of your cards are the same, would you like to split your hand? (y)es or (n)o") 
        if "y" in splitq.lower():
            playersCards2.append(playersCards.pop(1))
            playerTotal -= readCard(playersCards2[0])
            playerTotal2 += readCard(playersCards2[0])

            chosenCard = drawCard(playersCards)
            playerTotal += chosenCard[1]
  
            chosenCard = drawCard(playersCards2)
            playerTotal2 += chosenCard[1]        

            playersHandsList.append(playersCards)
            playersHandsList.append(playersCards2)

            playersHand = ', '.join(str(card) for card in playersCards)
            playersHand2 = ', '.join(str(card) for card in playersCards2)
            print(f"You now have 2 hands:\nHand 1 is {playersHand}. Total Value {playerTotal}\nHand 2 is {playersHand2} Total value {playerTotal2} ")
    else:
        playersHandsList.append(playersCards)


    #draw and remove 2 cards for pc
    for card in range(2):                               #Draw 2 cards for the dealer
        chosenCard = drawCard(pcCards)                  #Pick a card and return the card and its value
        pcTotal += chosenCard[1]                        #Add the value to the dealer's total hand value
    pcHand = ', '.join(str(card) for card in pcCards)   #turns the list of cards into a string

################## INITIAL DRAW ####################
    def requestInput(): 
        validAction = False
        while validAction != True:
            action = input("Would you like to (s)tick or (t)wist? ") 
            if action.lower() == "t" or action.lower() == "twist" or action.lower() == "hit" or action.lower().strip() == "hitme":
                validAction = True
            elif action.lower() == "s" or action.lower() == "stick" or action.lower() == "stand":
                validAction = True
        return action

    def playerTurn(playerTotal,playersCards):
        global playerPlaying
        playerBusted = False
        while playerPlaying == True:  
            action = requestInput()                            #Ask the player if they want to stick or twist

            if action.lower() == "t" or action.lower() == "twist" or action.lower() == "hit":   #if the action is twist
                chosenCard = drawCard(playersCards)                                             #Pick a card and return the card and its value
                playerTotal += chosenCard[1]                                                    #add the cards value to the player's total hand value
                print(f"You have drawn {chosenCard[0]}")                                        #tell the player the drawn card
                print(f"Your hand value is {playerTotal}")                                      #tell the player their total hand value
            else:                                                                               #if the input is anything other than twist consider it a stick.
                playerPlaying = False                                                           #set playerPlaying to false to break the while loop


            if playerTotal > 21:                                                                #if the player's hand value goes over 21
                playerPlaying = False                                                           #stop the player from playing
                playerBusted = True                                                             #set playerBusted to true
                print(f"Your hand value is {playerTotal}. BUSTED")                              #tell the player they have busted their hand
            elif playerTotal == 21:                                                             #if the player's hand reaches 21
                print(f"Your hand value is {playerTotal}!")                                     #tell them their hand value
                playerPlaying = False                                                           #stop the player from playing
        return playerBusted                                                    


    ## PLAYER'S TURN ##
                                                        #While its the player's turn
    result = playerTurn(playerTotal,playersCards)
    playerBusted = result
    if playerTotal2 > 0:
        result = playerTurn(playerTotal2,playersCards2)
        playerBusted2 = result

## DEALER'S TURN ##
    t.sleep(2)                                  #sleep the script
    print("\nIts now the dealers turn")         #confirm it's now the Dealer's turn
    t.sleep(1)                                  #sleep the script
    print(f"\nThe dealer drew {pcHand}")        #show the player the dealer's hand
    print(f"Their hand value is {pcTotal}")     #tell the player the Dealer's hand value
    t.sleep(3)                                  #sleep the script

    while pcPlaying == True:                                            #While its the Dealer's turn...

        if playerBusted == False or playerTotal2 > 0 and playerBusted2 == False:             #If the player is not bust...

            if pcTotal >= 17:                                           #If the Dealer's hand is 17 or more...
                pcPlaying = False                                       #the Dealer stops playing

                if pcTotal > 21:                                        #If the Dealer's hand is over 21...
                    pcBusted = True                                     #set pcBusted to true
                    print("The Dealer BUSTED!")                         #tell the player that the dealer has busted their hand

            else:                                                       #If the dealer's hand is < 17...
                print("\nThe Dealer will take a card")                  #confirm the dealer will take a card
                t.sleep(1)                                              #sleep the script
                chosenCard = drawCard(pcCards)                          #Pick a card and return the card and its value
                pcTotal += chosenCard[1]                                #add the cards value to the dealer's hand value
                print(f"The Dealer drew the {chosenCard[0]}")           #tell the player the drawn card
                t.sleep(1)                                              #sleep the script
                print(f"The Dealer's hand value is {pcTotal}")          #tell the player the dealer's hand value
                t.sleep(3)                                              #sleep the script

        else:                                                           #Else the player must already be bust...
            print("As your hand is busted the dealer will stick.")      #confirm to the player there is no point in the dealer drawing cards
            pcPlaying = False                                           #dealer stops playing
            t.sleep(1)                                                  #sleep the script

## WHEN BOTH THE DEALER AND PLAYER HAVE HAD THEIR TURNS##
    while pcPlaying == False and playerPlaying == False:                                            #While nether player are playing...
        if (playerTotal > pcTotal and playerTotal < 22) or (playerTotal2 > pcTotal and playerTotal2 < 22):                                              #If the playerTotal higher than the dealer's and the hand isn't bust...
            wins += 1                                                                               #add a win to the wins total
            gamesPlayed += 1                                                                        #add a game to the games played total
            print(f"You win this had! Well done. That makes {wins} wins and {losses} losses.")      #tell the player they have won
            resetGame()                                                                             #reset the game to initial settings
            playAgain()                                                                             #ask the player if they would like to play again.

        elif pcBusted == True and playerBusted == False or playerTotal2 > 0 and pcBusted == True and playerBusted2 == False:                                            #however if tge dealer is bust and the player isn't...
            wins += 1                                                                               #add a win to the wins total
            gamesPlayed += 1                                                                        #add a game to the games played total
            print(f"You win this had! Well done. That makes {wins} wins and {losses} losses.")      #tell the player they have won
            resetGame()                                                                             #reset the game to initial settings
            playAgain()                                                                             #ask the player if they would like to play again.

        elif playerTotal == pcTotal and playerBusted == False or playerTotal2 == pcTotal and playerBusted2 == False:                                      #However if the player's hand value is the same as the Dealer's and nether are bust
            gamesPlayed += 1                                                                        #add a game to the total games played
            print(f"Both the you and the Dealer have {playerTotal}. The hand is a tie.")            #confirm a draw
            resetGame()                                                                             #reset the game to initial settings
            playAgain()                                                                             #ask the player if they would like to play again.
            
        else:                                                                                       #If none of the above are true
            losses += 1                                                                             #add a game to the losses
            gamesPlayed += 1                                                                        #add a game to the games played
            print(f"\nThe house wins this time, Sorry. That is {wins} wins and {losses} losses.")   #tell the player they lost
            resetGame()                                                                             #reset the game to initial settings
            playAgain()                                                                             #ask the player if they would like to play again.
              

print("\n\nThanks for playing Daniel's Blackjack!")
t.sleep(1)
print("Your performance breakdown:")
print(f"You played {gamesPlayed} Hands and won {wins} of them, lost {losses} of them and tied {gamesPlayed - (wins + losses)} hands. ")
t.sleep(1)
if wins > losses:
    print("You won more than you lost! Well done. Now you are ready to do it for real.")
else:
    print("Looks like you need a little more practice.")

print("See you again soon.")


    


#evaluate pc cards

#pc takes acton 

#find winner
