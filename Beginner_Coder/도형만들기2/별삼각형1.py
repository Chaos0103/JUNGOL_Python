def type_01(Height):
    for i in range(Height):
        for _ in range(i + 1):
            print('*', end='')
        print('')

def type_02(Height):
    for i in range(Height):
        for _ in range(Height - i):
            print('*', end='')
        print('')

def type_03(Height):
    star = 1
    blank = Height - 1
    for _ in range(Height):
        for _ in range(blank):
            print(' ', end='')
        for _ in range(star):
            print('*', end='')
        print('')
        star += 2
        blank -= 1

height, type = map(int, input().split())

if not(0 < height and height <= 100):
    print('INPUT ERROR!')
else:
    if type == 1:
        type_01(height)
    elif type == 2:
        type_02(height)
    elif type == 3:
        type_03(height)
    else:
        print('INPUT ERROR!')
