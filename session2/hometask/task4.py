player1 = input("Please enter rock/paper/scissors:" )

player2 = input("Please enter rock/paper/scissors:" )


if player1 == "rock" and player2 == "scissors":
    print("Player1 wins")
elif player1 == "scissors" and player2 == "paper":
    print("Player1 wins")
elif player1 == "rock" and player2 == "paper":
    print("Player2 wins")
elif player1 == "scissors" and player2 == "rock":
    print("Player2 wins")
elif player1 == "paper" and player2 == "rock":
    print("Player1 wins")
elif player1 == "paper" and player2 == "scissors":
    print("Player2 wins")
elif player1 == player2:
    print("It's a tie")
