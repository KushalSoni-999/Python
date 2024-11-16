from tabulate import tabulate
import computer

board = [
    [" " , " " , " "],
    [" ", " " , " "],
    [" " , " " , " "],
]

# Checking if a player has won the game
def game_over(x,y):
    x = int(x)
    y = int(y)
    if [x,y] in [[0,0],[2,2]]:
        if board[0][0] == board[1][1] == board[2][2]:
            return True
    elif [x,y] in [[0,2],[2,0]]:
        if board[0][2] == board[1][1] == board[2][0]:
            return True
    elif x == y:
        if (board[0][0] == board[1][1] == board[2][2]) | (board[0][2] == board[1][1] == board[2][0]):
            return True
    if (board[x][0] == board[x][1] == board[x][2]) | (board[0][y] == board[1][y] == board[2][y]):
            return True
    return False

# Defining options/choices for players
options = ['X', 'O']
#Asking user for number of players
No_players = int(input("Welcome enter number of players: "))
if No_players > 2 or No_players < 1:
    raise ValueError

if No_players == 2:
    #Prompting player1 to choose X or O
    while True:
            player1 = input("Player1, Choose X or O: ").upper()
            if player1 not in options:
                continue
            else:
                player2 = 'X' if player1 == 'O' else 'O'
                break

    print(f"Player1: {player1}, Player2: {player2}")

    turn = player1
    #Gameover used to check if the game is over and end the outer while loop
    gameover = False
    #Since the game can only have 9 turns, total_turns is used to keep track of the number of turns 
    total_turns = 0

    while total_turns<9 and not gameover:
        #Printing the board in every turn
        print("Board: ")
        print(tabulate(board,tablefmt="grid")) 
        total_turns += 1
        #While loop to keep asking for a valid move and if move is valid then update the board 
        # and check if the game is over after that move
        while True:
            if turn == player1:
                curr = "Player1"
            else:
                curr = "Player2"
            move = input(f"{curr} ({turn}) enter your move (row col): ")
            x,y = move.split()
            if board[int(x)][int(y)] == ' ':
                board[int(x)][int(y)] = turn
                last_move = move
                if game_over(x,y):
                    print(f"{turn} wins!")
                    print(tabulate(board,tablefmt="grid"))
                    gameover = True
                    break
                #After a valid move, the turn is switched to the other player
                if turn == player1:
                    turn = player2
                else:
                    turn = player1
                break
            else:
                print("Invalid move")
    # If the game is not over after 9 turns, then its a draw
    if not gameover:
        print("Its a draw!") 
        print(tabulate(board,tablefmt="grid"))
#If the number of players is 1, then the computer will play against the player
else:
    # Two players are defined where player2 will be the computer
    player1 = input("Player1, Choose X or O: ").upper()
    if player1 not in options:
        raise ValueError("Invalid input")
    else :
        if player1 == 'X':
            player2 = computer.Computer('O')
        else:
            player2 = computer.Computer('X')
    print(f"Player1: {player1}, Player2: Computer")
    #Player1 will always start the game
    turn = player1
    #Gameover used to check if the game is over and end the outer while loop
    gameover = False
    #Since the game can only have 9 turns, total_turns is used to keep track of the number of turns
    total_turns = 0
    while total_turns<9 and not gameover:
        #Printing the board in every turn
        print("Board: ")
        print(tabulate(board,tablefmt="grid")) 
        total_turns += 1
        #While loop to keep asking for a valid move and if move is valid then update the board
        # and check if the game is over after that move
        while True:
            if turn == player1:
                curr = "Player1"
            else:
                curr = "Computer"
            #If its player1's turn, then player1 will enter the move
            if curr == "Player1":
                move = input(f"{curr} ({turn}) enter your move (row col): ")
                x,y = move.split()
                if board[int(x)][int(y)] == ' ':
                    board[int(x)][int(y)] = turn
                    if game_over(x,y):
                        print(f"{curr} wins!")
                        print(tabulate(board,tablefmt="grid"))
                        gameover = True
                        break
                    #After a valid move, the turn is switched to the other player remember here player2 is computer
                    else:
                        turn = player2
                        break
                else:
                    print("Invalid move")
            #If its computer's turn, then computer will enter the move by calling get_move method from computer.py
            else:
                move = player2.get_move(board)
                board[move[0]][move[1]] = player2.letter
                if game_over(move[0],move[1]):
                    print(f"{curr} wins!")
                    print(tabulate(board,tablefmt="grid"))
                    gameover = True
                    break
                turn = player1
                break
    # If the game is not over after 9 turns, then its a draw
    if not gameover:
        print("Its a draw!") 
        print(tabulate(board,tablefmt="grid"))






    

    
    