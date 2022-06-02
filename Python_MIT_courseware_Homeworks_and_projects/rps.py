x = 1

while x <= 4:
    player1 = input("Player 1 ?")
    player2 = input("Plyaer 2 ?")

    if (player1 == player2):
        print("Tie")
    elif(player1 == "rock"):
        if(player2 == "paper"):
            print ("Player 2 wins")
        elif(player2 == "scissors"):
            print ("Player 1 wins")
    elif(player1 == "paper"):
        if(player2 == "rock"):
            print ("Player 1 wins")
        elif(player2 == "scissors"):
            print("Player 2 wins")
    elif(player1 == "scissors"):
        if(player2 == "rock"):
            print("Player 2 wins")
        elif(player2 == "paper"):
            print("Player 1 wins")
    x+=1
