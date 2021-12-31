import random
playerOptions = {"rock":"a", "paper":"b", "scissors":"c"}
#          rock  paper scissors
pcOptions = {"rock":"ab", "paper":"bc", "scissors":"ca"}

pcPlays = random.choice(list(pcOptions))
playerPlays = playerOptions[input("rock paper scissors? ")]

print(f"Your opponent drew {pcPlays}")
if playerPlays not in pcOptions[pcPlays]:
    print("You lose!")
elif pcOptions[pcPlays].find(playerPlays) == 1:
    print("You win!")
else:
    print("Draw")