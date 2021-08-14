num = list(map(int, input().split()))
sum = 0

for idx in range(len(num)):
    sum += num[idx]

print('%.2f' % (sum / len(num)))
