import random

class Throw:
    def __init__(self, name, beats):
        self.name = name
        self.beats = beats

rock = Throw("rock", "scissors")
paper = Throw("paper","rock")
scissors = Throw("scissors","paper")

throws = [rock, paper, scissors]

opponentPlays = random.choice(throws)
playerPlays = input("rock paper or scissors? ")

print("Your opponent plays " + getattr(opponentPlays, "name"))

if playerPlays in getattr(opponentPlays, "beats"):
    print("Opponent Wins!")
elif playerPlays in getattr(opponentPlays, "name"):
    print("Draw!")
else:
    print("Player Wins!")

print(getattr(opponentPlays, "name"))