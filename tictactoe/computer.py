import random 
class Computer:
    def __init__(self, letter):
        self.letter = letter
        if self.letter == 'X':
            self.opponent = 'O'
        else:
            self.opponent = 'X'
    def get_move(self, board):
        # Checking if the computer can win in the next move
        if checkifwin(board, self.letter) != None:   
            x , y = checkifwin(board, self.letter).split()
            return int(x),int(y)
        # Checking if the opponent can win in the next move
        elif checkifwin(board, self.opponent) != None:
            x , y = checkifwin(board, self.opponent).split()
            return int(x),int(y)
        # Making compute to move losesly to its previous moves to possibly win
        elif possiblewin(board , self.letter) != None:
            x, y = possiblewin(board , self.letter)
            return int(x),int(y)
        # At last if neither of the above conditions are met, the computer will make a random move 
        else:
            [x,y] = random.choice([(i, j) for i, row in enumerate(board) for j, cell in enumerate(row) if cell == " "])
            return int(x),int(y)
            


def checkifwin(board, player):
    moves = [(i, j) for i, row in enumerate(board) for j, cell in enumerate(row) if cell == f"{player}"]
    x_done = set(i for i, j in moves)
    y_done = set(j for i, j in moves)
    for i in x_done:
        if board[i][0] == board[i][1] == player and board[i][2] == " ":
            return f"{i} 2"
        if board[i][0] == board[i][2] == player and board[i][1] == " ":
            return f"{i} 1"
        if board[i][1] == board[i][2] == player and board[i][0] == " ":
            return f"{i} 0"
    for j in y_done:
        if board[0][j] == board[1][j] == player and board[2][j] == " ":
            return f"2 {j}"
        if board[0][j] == board[2][j] == player and board[1][j] == " ":
            return f"1 {j}"
        if board[1][j] == board[2][j] == player and board[0][j] == " ":
            return f"0 {j}"
    if board[0][0] == board[1][1] == player and board[2][2] == " ":
        return "2 2"
    if board[0][0] == board[2][2] == player and board[1][1] == " ":
        return "1 1"
    if board[1][1] == board[2][2] == player and board[0][0] == " ":
        return "0 0"
    if board[0][2] == board[1][1] == player and board[2][0] == " ":
        return "2 0"
    if board[0][2] == board[2][0] == player and board[1][1] == " ":
        return "1 1"
    if board[1][1] == board[2][0] == player and board[0][2] == " ":
        return "0 2"
    else:
        return None
def possiblewin(board , player):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = player
                if checkifwin(board, player) != None:
                    board[i][j] = " "
                    return i,j
                board[i][j] = " "
