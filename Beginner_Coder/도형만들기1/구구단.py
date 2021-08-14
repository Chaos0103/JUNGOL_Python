while True:
    start, end = map(int, input().split())
    if not (2 <= start <= 9 and 2 <= end <= 9):
        print('INPUT ERROR!')
        continue
    break

dan = list()

if start >= end:
    while not(start < end):
        dan.append(start)
        start -= 1
else:
    while not(start > end):
        dan.append(start)
        start += 1

for i in range(1, 10):
    for j in dan:
        print(j, '*', i, '=', '%2d' % (i * j), end='   ')
    print('')
