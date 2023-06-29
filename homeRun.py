# main code
from rollDice import *
from Walkthrough import *
countA = 0
countB = 0
flag="A"

while (countA <30 and countB <30):
    if flag=="A":
        roll=input("press 'y' to Roll a dice for Player A: ")
        if roll=="y":
            place =rollDice()
            countA=countA+place
            print("Player A : ", countA, "  |  ", "Player B: ", countB)
            print("\n")
            walkThrough(countA,countB)
        else:
            print("Thanks for choosing Home run to play")
        flag ="B"
    else:
        roll=input("press 'y' to Roll a dice for Player B: ")
        if roll=="y":
            place =rollDice()
            countB=countB+place
            print("Player A : ", countA, "  |  ", "Player B: ", countB)
            print("\n")
            walkThrough(countA,countB)
        flag= "A"

print("Welcome Home")
if countA>=30:
    print ("Winner of the Game is Player A")
else:
    print ("Winner of the Game is Player B")




