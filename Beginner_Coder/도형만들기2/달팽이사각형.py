G_FRONT_IDX = 0
G_BACK_IDX = -1
G_NUM = 0

def IDX(FIdx, BIdx):
    global G_FRONT_IDX
    global G_BACK_IDX
    global G_NUM
    G_FRONT_IDX += FIdx
    G_BACK_IDX += BIdx
    G_NUM += 1

def Right(NumList):
    IDX(0, 1)
    NumList[G_FRONT_IDX][G_BACK_IDX] = G_NUM

def Down(NumList):
    IDX(1, 0)
    NumList[G_FRONT_IDX][G_BACK_IDX] = G_NUM

def Left(NumList):
    IDX(0, -1)
    NumList[G_FRONT_IDX][G_BACK_IDX] = G_NUM

def Up(NumList):
    IDX(-1, 0)
    NumList[G_FRONT_IDX][G_BACK_IDX] = G_NUM

size = int(input())

num = [[1] * size for _ in range(size)]

if size % 2 == 1:
    printCnt = size - 1
    while True:
        if printCnt == 0:
            Right(num)
            break
        for _ in range(printCnt + 1):
            Right(num)
        for _ in range(printCnt):
            Down(num)
        for _ in range(printCnt):
            Left(num)
        for _ in range(printCnt - 1):
            Up(num)
        printCnt -= 2
else:
    printCnt = size - 1
    while True:
        if printCnt < 0:
            break
        for _ in range(printCnt + 1):
            Right(num)
        for _ in range(printCnt):
            Down(num)
        for _ in range(printCnt):
            Left(num)
        for _ in range(printCnt - 1):
            Up(num)
        printCnt -= 2
for i in range(size):
    for j in range(size):
        print(num[i][j], end=' ')
    print('')
