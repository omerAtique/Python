
# Name:
# Section:
# nims.py

def play_nims(pile, max_stones):
    
    while pile >= 0:
        player1 = int(input("Enter the number of stones choosen by player 1: "))
        
        while not(player1 >=1 and player1 <=max_stones):
            print("INVALID NUMBER OF STONES. TRY AGAIN.")
            player1 = int(input("Enter a valid number of stones choosen by player 1: "))
        pile-=player1
        if pile <=0:
            print("Player 1 wins!!!")
            break
        player2 = int(input("Enter the number of stones choosen by player 2: "))
        
        while not(player2 >=1 and player2 <=max_stones):
            print("INVALID NUMBER OF STONES. TRY AGAIN.")
            player2 = int(input("Enter a valid number of stones choosen by player 2: "))
        pile-=player2
        if pile <=0:
            print("Player 2 wins!!!")
            break

    print("GAME OVER!!!")


play_nims(20, 5)

    ## Basic structure of program (feel free to alter as you please):

#    while [pile is not empty]:
#        while [player 1's answer is not valid]:
#            [ask player 1]
#            [execute player 1's move]
#       
#        while [player 2's answer is not valid]:
#            [ask player 2]
#            [execute player 2's move]
#
#    print "Game over"