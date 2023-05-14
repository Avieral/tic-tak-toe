board=["_","_","_",
    "_","_","_",
    "_","_","_"]
currentplayer="X"
winner=None
gameRunning=True
def printboard(board):
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("------")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("------")
    print(board[6]+" | "+board[7]+" | "+board[8])
def playerInput(board):
    inp=int(input("Enter a number 1-9-"))
    if inp >=1 and inp<=9 and board[inp-1]=="_":
        board[inp-1]=currentplayer
    else:
        print("Not possible to mark")
        
def checkhorizontal(board):
    global winner,a
    if board[0]==board[1]==board[2] and board[1]!="_":
        winner =board[0]
        return True
    elif board[3]==board[4]==board[5] and board[4]!="_":
        winner=board[3]
        return True
    elif board[6]==board[7]==board[8] and board[7]!="_":
        winner=board[6]
        return True
def checkrow(board):
    global winner,b
    if board[0]==board[3]==board[6] and board[3]!="_":
        winner=board[0]
        return True
    elif board[7]==board[4]==board[1] and board[1]!="_":
        winner=board[1]
        return True
    elif board[2]==board[5]==board[8] and board[2]!="_":
        winner=board[2]
        return True
def checkdiag(board):
    global winner,c
    if board[0]==board[4]==board[8] and board[0]!="_":
        winner=board[0]
        return True
    elif board[2]==board[4]==board[6] and board[2]!="_":
        winner=board[2]
        return True
def tie(board):
    if "_" not in board:
        printboard(board)
        print("its tie")
        gameRunning=False
def switchplayer():
    global currentplayer
    if currentplayer=="X":
        currentplayer="O"
    else:
        currentplayer="X"
        
def checkWin():
    if checkhorizontal(board) or checkrow(board) or checkdiag(board):
        print(f"The winner is {winner}") 
        gameRunning=False
        printboard(board)
        if gameRunning==False:
            quit()
        
while gameRunning:
    printboard(board)
    playerInput(board)
    checkWin()
    tie(board)
    switchplayer()
