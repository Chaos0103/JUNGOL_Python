sum = 0
cnt = 0

while True:
    num = int(input())
    sum += num
    cnt += 1
    if num >= 100:
        break

print(sum)
print('%.1f' % (sum / cnt))
