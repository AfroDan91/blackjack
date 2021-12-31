# Orc beats human,elf
# Human beats Elf,Dwarf
# Elf beats Dwarf,Dragonborn
# Dwarf beats Dragonborn, Orc
# Dragonborn beats Orc, Human
import random
from typing import Counter

orcs = ["orc", "human", "elf", "Orcs"]
humans = ["human", "elf", "dwarf", "Humans"]
elves = ["elf", "dragonborn", "dwarf", "Elves"]
dwarves = ["dwarf", "dragonborn", "orc", "Dwarves"]
dragonborn = ["dragonborn", "orc", "human", "Dragonborn"]
race = [orcs,humans,elves,dwarves,dragonborn]
playerscore = 0
pcscore = 0
ready = False
validthrow = False
##Intro
print (" ##########################################################################################\n\n\n\n\nWelcome to the tactical masterclass of 5 armies, I am Elio. The best in all the land.\n")
playername = input("Whom is my opponent?\n ")
print (f"Haha, who names their child {playername}?\nDoesnt matter, prepare to be crushed.")

##GameSetup
while ready == False:
    bestof = int(input("\nFirst to 3 or 5?\n "))    
    if bestof == 3:
      print ("Ah yes, finish this quickly. I am a busy man after all\n")
      ready = True
    elif bestof == 5:
      print ("Ah yes, I like to take my time\n")
      ready = True
    else:
        print ("Well this is going to be easier than I thought, Try this again first to 3 or first to 5\n")
        ready = False

##Rules explanation
rules= input("Well then, let us begin! I assume even you know the rules?\nY or N\n " )
if rules.lower() == ("n"):
    print("What kind of school did you even go to?\nIts simple really Orcs beat the puny Elves and Humans\nHumans, as always cheat the Elves and the Dwarves\nElves archane abilities best the Dwarves and the Dragonborn\nDwarven technology smites the Dragonborns and the Orcs\nAnd finally the Dragonborn outwit the dim Orcs and equally dim Humans\nAnyway, Enough talking. lets play! ")
else:
    print(f"Ok then, first to {bestof} it is. Lets go!")
            
##Gameplay
Counter=0
while playerscore < int(bestof) or pcscore < int(bestof):      ################################################################
    print (playerscore)
    print(validthrow)
    while (validthrow == False):
        playerchoice = input("Orc,Human,Elf,Dwarf or Dragonborn?\n ")
        if playerchoice.lower() == "orc":
            validthrow = True
        elif playerchoice.lower() == "human":
            validthrow = True
                                                    #########################NEED HELP##############################
        elif playerchoice.lower() == "dragonborn":
            validthrow = True
        
        elif playerchoice.lower() == "dwarf":
            validthrow = True
        
        elif playerchoice.lower() == "elf":
            validthrow = True                                               ##################################################################
        
        else: print("Invalid Unit, Try again.\n")
            
    pcchoice = random.choice(race)
    if playerchoice.lower() in pcchoice:    
        if playerchoice.lower() in pcchoice[0]:
            print (f"I choose an army of {pcchoice[3]}, Its a tie!\n")
            validthrow = False
                
        else: 
            print (f"I choose an army of {pcchoice[3]}, You lose!")
            pcscore += 1
            print(f"I currently have {pcscore} wins\n")
            validthrow = False
                
    else:  
        print (f"I choose an army of {pcchoice[3]}, You win!")
        playerscore += 1
        print(f"You currently have {playerscore} wins\n")
        validthrow = False
            
        

        
        
                


##Scorekeeping    
if Counter == 3:
    print (f"If I knew beating you was going to be this easy {playername}, I wouldn't have even got out of bed this morning")
else: 
    print (f"What?!? This is impossible. You must be cheating. What are you hiding {playername}?")