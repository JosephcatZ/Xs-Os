board = [
            [' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' ']
        ]
Turn = 'X'
def drawBoard(board):
    y = 0
    for i in board:
        out = ''
        for j in i:
            out = out + str(j)+'|'
        print(out[0:5])
        y=y+1
        if y < len(board):
            print("-+-+-")
