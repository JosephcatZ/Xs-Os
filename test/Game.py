import setup as var
board = var.board
#var.DrawBoard(var.board)

def Xplay(pos,width,board):
    i = board[((pos/width)-((pos/width)%1))][pos%width-1]
    print(board[((pos/width)-((pos/width)%1))])
    if i == ' ':
        board[(pos/width)-((pos/width)%1)][pos%width-1] = "X"

def Oplay(pos,width,board):
    i = board[((pos/width)-((pos/width)%1))][pos%width-1]
    print(board[((pos/width)-((pos/width)%1))])
    if i == ' ':
        board[(pos/width)-((pos/width)%1)][pos%width-1] = "O"

Oplay(1,3,var.board)
var.drawBoard(board)

