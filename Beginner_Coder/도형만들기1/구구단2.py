start, end = map(int, input().split())

if start > end:
    dan = start + 1
else:
    dan = start - 1

while not(end == dan):
    if start > end:
        dan -= 1
    else:
        dan += 1
    for i in range(1, 10):
        print('%d * %d = %2d' % (dan, i, dan * i), end='   ')
        if i % 3 == 0:
            print('')
    print('')
