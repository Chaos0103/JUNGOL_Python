def type_01(Height):
    num = [[0] * Height for _ in range(Height)]
    inNum = 1
    for i in range(Height):
        for j in range(i + 1):
            if i % 2 == 0:
                num[i][j] = inNum
            else:
                num[i][i - j] = inNum
            inNum += 1
    for i in range(Height):
        for j in range(i + 1):
            print(num[i][j], end=' ')
        print('')

def type_02(Height):
    star = Height * 2 - 1
    blank = 0
    for i in range(Height):
        for _ in range(blank):
            print(' ', end=' ')
        for _ in range(star):
            print(i, end=' ')
        print('')
        star -= 2
        blank += 1

def type_03(Height):
    star = 1
    for i in range(Height):
        for j in range(star):
            print(j + 1, end=' ')
        print('')
        if i >= Height // 2:
            star -= 1
        else:
            star += 1

height, type = map(int, input().split())

if not(1 <= height and height <= 100) or not(height % 2 == 1):
    print('INPUT ERROR!')
elif not(1 <= type and type <= 3):
    print('INPUT ERROR!')
else:
    if type == 1:
        type_01(height)
    elif type == 2:
        type_02(height)
    elif type == 3:
        type_03(height)
