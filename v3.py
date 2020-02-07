# import random

from random import randint
# print("Rock...")
# print("Paper...")
# print("Scissors...")

player1 = input("Player, make your move: ").lower()
# rand_num = random.randint(0,2)
rand_num = randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print(f"Computer plays {computer}")
    
if player1 == computer:
    print("it's a tie!")
elif player1 == "rock":
    if computer == "scissors":
        print("player wins!")
    else:
        print("computer wins!")
elif player1 == "paper":
    if computer == "rock":
        print("player wins")
    # elif computer == "scissors":
    else:
        print("player wins")
elif player1 == "scissors":
    if computer == "rock":
        print("computer wins!")
    # elif computer == "paper":
    else:
        print("player wins!")
else:
    print("something went wrong")