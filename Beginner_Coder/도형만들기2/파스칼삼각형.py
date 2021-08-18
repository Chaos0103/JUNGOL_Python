def triangle(Height, TriList):
    for i in range(Height):
        for j in range(i + 1):
            if (i == j) or (j == 0):
                TriList[i][j] = 1
            else:
                TriList[i][j] = TriList[i - 1][j - 1] + TriList[i - 1][j]

def type_01(Height, TriList):
    for i in range(Height):
        for j in range(i + 1):
            print(TriList[i][j], end=' ')
        print('')

def type_02(Height, TriList):
    for i in range(Height):
        for _ in range(i):
            print(end=' ')
        for j in range(Height - i):
            print(TriList[Height - 1 - i][j], end=' ')
        print('')

def type_03(Height, TriList):
    for i in range(Height):
        for j in range(i + 1):
            print(TriList[Height - 1 - j][Height - 1 - i], end=' ')
        print('')

height, type = map(int, input().split())

triList =[[0] * height for _ in range(height)]

triangle(height, triList)

if type == 1:
    type_01(height, triList)
elif type == 2:
    type_02(height, triList)
elif type == 3:
    type_03(height, triList)
