def LD(ChList): #Left_Down
    IdxMove(1, -1)
    MakeResult(ChList)

def RD(ChList): #Right_Down
    IdxMove(1, 1)
    MakeResult(ChList)

def RU(ChList): #Right_Up
    IdxMove(-1, 1)
    MakeResult(ChList)

def LU(ChList): #Left_Up
    IdxMove(-1, -1)
    MakeResult(ChList)

def IdxMove(FIdx, BIdx):
    global FRONTIDX
    global BACKIDX
    global GCHAR
    FRONTIDX += FIdx
    BACKIDX += BIdx
    GCHAR = chr(ord(GCHAR) + 1)
    if GCHAR > 'Z':
        GCHAR = 'A'

def MakeResult(ChList):
    ChList[FRONTIDX][BACKIDX] = GCHAR

size = int(input())
cnt = size - 1
size = size * 2 - 1

FRONTIDX = -1
BACKIDX = cnt + 1
GCHAR = chr(ord('A') - 1)

ch = [[' '] * size for _ in range(size)]

while True:
    for _ in range(cnt + 1):
        LD(ch)
    if cnt == 0:
        break
    for _ in range(cnt):
        RD(ch)
    for _ in range(cnt):
        RU(ch)
    for _ in range(cnt - 1):
        LU(ch)
    FRONTIDX -= 1
    cnt -= 1

for i in range(size):
    for j in range(size):
        print(ch[i][j], end=' ')
    print('')
