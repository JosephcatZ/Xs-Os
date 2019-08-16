import setup as var
board = var.board
#var.DrawBoard(var.board)

def Xplay(pos,width,board):
    i = board[((pos/width)-((pos/width)%1))][pos%width]
    #print(board[((pos/width)-((pos/width)%1))])
    if i == ' ':
        board[(pos/width)-((pos/width)%1)][pos%width] = "X"

def Oplay(pos,width,board):
    i = board[((pos/width)-((pos/width)%1))][pos%width]
    #print(board[((pos/width)-((pos/width)%1))])
    if i == ' ':
        board[(pos/width)-((pos/width)%1)][pos%width] = "O"

def Rwin(r,board):
        x = board[r-1][0]
        ret = True
        for i in board[r-1]:
                if i != x:
                        ret = False
        return(ret)
def WinValR(r,board):
        if(Rwin(r,board)):
                return(board[r-1][0])
        else:
                return(None)


def Cwin(r,board):
        x = board[0][r-1]
        ret = True
        for i in board:
                
                if i[r-1] != x:
                        ret = False
        return(ret)
def WinValC(c,board):
        if(Cwin(c,board)):
                return(board[0][c-1])
        else:
                return(None)

def Dwin(board):
        if(board[0][0]==board[1][1]==board[2][2] or board[0][2]==board[1][1]==board[2][0]):
                return(True)
        return(False)
def WinValD(board):
        if(Dwin(board)):
                return(board[1][1])
        else:
                return(None)
def Winner(board):
        if WinValD(board) != None:
                return(WinValD(board))
        if WinValR(1,board) != None:
                return(WinValR(1,board))
        if WinValR(2,board) != None:
                return(WinValR(2,board))
        if WinValR(3,board) != None:
                return(WinValR(3,board))
        if WinValC(1,board) != None:
                return(WinValC(1,board))
        if WinValC(2,board) != None:
                return(WinValC(2,board))
        if WinValC(3,board) != None:
                return(WinValC(3,board))
        return(None)
        
Xplay(2,3,board)
Xplay(4,3,board)
Xplay(6,3,board)
var.drawBoard(board)
print(Winner(board))


