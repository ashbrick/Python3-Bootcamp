# Create a basic mini version of rock, paper, scissors using logic and conditionals

# Show welcome message
print("Let's play Rock, Paper, Scissors!")
# player 1 input
player1 = input("Enter Player 1's choice: ")

# player 2 input
player2 = input("Enter Play 2's choice: ")

print("SHOOT!")

# player1 winning scenarios
if player1 == 'rock' and player2 == 'scissors':   
    print("Player 1 wins!")
elif player1 == 'paper' and player2 == 'rock':
    print("Player 1 wins!")
elif player1 == 'scissors' and player2 == 'paper':
    print("Player 1 wins!")

# player 2 winning scenarios
elif player1 == 'paper' and player2 == 'scissors':
    print("Player 2 wins!")
elif player1 == 'rock' and player2 == 'paper':
    print("Player 2 wins!")
elif player1 == 'scissors' and player2 == 'rock':
    print("Player 2 wins!")

# tie scenarios
else:
    print("You tied... play again")