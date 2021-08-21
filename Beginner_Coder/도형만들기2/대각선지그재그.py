#함수
def RightUp(NumList):
    MoveIdx(-1, 1)
    NumList[FRONTIDX][BACKIDX] = GNUM
def LeftDown(NumList):
    MoveIdx(1, -1)
    NumList[FRONTIDX][BACKIDX] = GNUM
def Down(NumList):
    MoveIdx(1, 0)
    NumList[FRONTIDX][BACKIDX] = GNUM
def Right(NumList):
    MoveIdx(0, 1)
    NumList[FRONTIDX][BACKIDX] = GNUM
def MoveIdx(FIdx, BIdx):
    global FRONTIDX
    global BACKIDX
    global GNUM
    FRONTIDX += FIdx
    BACKIDX += BIdx
    GNUM += 1
#변수
FRONTIDX = 0
BACKIDX = -1
GNUM = 0
#입력
size = int(input())
numList = [[0] * size for _ in range(size)]
cnt = 0

for i in range(size * 2 - 1):
    if i % 2 == 0:
        if i < size:
            Right(numList)
        else:
            Down(numList)
        for _ in range(cnt):
            LeftDown(numList)
    else:
        if i < size:
            Down(numList)
        else:
            Right(numList)
        for _ in range(cnt):
            RightUp(numList)
    if i < size:
        cnt += 1
        if cnt == size:
            cnt = size - 2
    else:
        cnt -= 1

for i in range(size):
    for j in range(size):
        print(numList[i][j], end=' ')
    print('')
