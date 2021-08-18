def type_01(Height):
    star = 1
    for i in range(Height):
        for _ in range(star):
            print('*', end='')
        print('')
        if i >= Height // 2:
            star -= 1
        else:
            star += 1

def type_02(Height):
    blank = Height // 2
    star = 1
    for i in range(Height):
        for _ in range(blank):
            print(end=' ')
        for _ in range(star):
            print('*', end='')
        print('')
        if i >= Height // 2:
            star -= 1
            blank += 1
        else:
            star += 1
            blank -= 1

def type_03(Height):
    star = Height
    blank = 0
    for i in range(Height):
        for _ in range(blank):
            print(end=' ')
        for _ in range(star):
            print('*', end='')
        print('')
        if i >= Height // 2:
            star += 2
            blank -= 1
        else:
            star -= 2
            blank += 1

def type_04(Height):
    star = Height // 2 + 1
    blank = 0
    for i in range(Height):
        for _ in range(blank):
            print(end=' ')
        for _ in range(star):
            print('*', end='')
        print('')
        if i >= Height // 2:
            star += 1
        else:
            star -= 1
            blank += 1

height, type = map(int, input().split())

if not(0 <= height and height <= 100) or (height % 2 == 0):
    print('INPUT ERROR!')
elif not(1 <= type and type <= 4):
    print('INPUT ERROR!')
else:
    if type == 1:
        type_01(height)
    elif type == 2:
        type_02(height)
    elif type == 3:
        type_03(height)
    elif type == 4:
        type_04(height)
