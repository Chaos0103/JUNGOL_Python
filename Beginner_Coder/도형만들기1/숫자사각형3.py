size = int(input())

num = [[0] * size for _ in range(size)]
inNum = 1

for i in range(size):
    for j in range(size):
        num[j][i] = inNum
        inNum += 1

for i in range(size):
    for j in range(size):
        print(num[i][j], end=' ')
    print('')
