board = [
    ["-", "-", "-", "-", "-", "-", "-", "-",],
    ["-", "-", "-", "-", "-", "-", "-", "-",],
    ["-", "-", "-", "-", "-", "-", "-", "-",],
    ["-", "-", "-", "-", "-", "-", "-", "-",],
    ["-", "-", "-", "-", "-", "-", "-", "-",],
    ["-", "-", "-", "-", "-", "-", "-", "-",],
    ["-", "-", "-", "-", "-", "-", "-", "-",],
    ["-", "-", "-", "-", "-", "-", "-", "-",],
]


startposX=int(input("Input Starting X position between 0 and 7 "))
startposY=int(input("Input Starting Y position between 0 and 7 "))
board[startposY][startposX]='X'

#def takeStopPosition():
stopposX=int(input("Input Stopping X position between 0 and 7 "))
stopposY=int(input("Input Stopping Y position between 0 and 7 "))
board[stopposY][stopposX]='Z'

currentX=startposX
currentY=startposY
a=stopposY-startposY
b=stopposX-startposX

def moveUp(int):
    for i in range(0,int,-1):
        board[startposY+i-1][startposX]="+"

def moveDown(int):
    for i in range(int):
        board[startposY+i+1][startposX]="+"

def moveLeft(int):
    for i in range(0,int,-1):
        board[startposY+a][startposX+i-1]="+"

def moveRight(int):
    for i in range(int):
        board[startposY+a][startposX+i+1]="+"

def route():
   pass 

def main():
    if a>=0:
        moveDown(a)
    else:
        moveUp(a)
    if b>=0:
        moveRight(b)
    else:
        moveLeft(b)
    #takeStartPosition()
    #takeStopPosition()
    for i in range(len(board)):
        print(board[i])
    
    

if __name__ == '__main__':
    main()
