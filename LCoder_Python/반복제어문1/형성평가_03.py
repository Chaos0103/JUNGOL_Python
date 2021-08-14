sum = 0
cnt = 0

while True:
    num = int(input())
    if not(0 <= num <= 100):
        break
    sum += num
    cnt += 1

print('sum :', sum)
print('avg : %.1f' % (sum / cnt) )
