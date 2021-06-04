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


startPosX = int(input("give a start position on X axis (between 0 and 7)\n"))
startPosY = int(input("give a start position on y axis (between 0 and 7)\n"))
board[startPosY][startPosX] = 'S'

stopPosX = int(input("give a stop position on X axis (between 0 and 7)\n"))
stopPosY = int(input("give a stop position on y axis (between 0 and 7)\n"))
board[stopPosY][stopPosX] = 'F'


currentX = startPosX
currentY = startPosY
a = stopPosY - startPosY
b = stopPosX - startPosX

# def moveUp(int):
#     for i in range(0,int,-1):
#         board[startPosY - 1 + i][startPosX] = "+"


# def moveDown(int):
#     for i in range(int):
#         board[startPosY + 1 + i][startPosX] = "+"
#     #print("Down, " + int)


# def moveLeft(int):
#     for i in range(0,int,-1):
#         board[startPosY+a][startPosX - 1 + i] = "+"


# def moveRight(int):
#     for i in range(int):
#         board[startPosY+a][startPosX + 1 + i] = "+"

def moveUp(int):
    for i in range(0,int,-1):
        board[startPosY+i-1][startPosX]="+"

def moveDown(int):
    for i in range(int):
        board[startPosY+i+1][startPosX]="+"

def moveLeft(int):
    for i in range(0,int,-1):
        board[startPosY+a][startPosX+i-1]="+"

def moveRight(int):
    for i in range(int):
        board[startPosY+a][startPosX+i+1]="+"

    

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
    