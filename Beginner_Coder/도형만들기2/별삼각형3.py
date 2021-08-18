height = int(input())

if not(1 <= height and height <= 100) or not(height % 2 == 1):
    print('INPUT ERROR!')
else:
    star = 1
    blank = 0

    for i in range(height):
        for _ in range(blank):
            print(end=' ')
        for _ in range(star):
            print('*', end='')
        print('')

        if i >= height // 2:
            blank -= 1
            star -= 2
        else:
            blank += 1
            star += 2
