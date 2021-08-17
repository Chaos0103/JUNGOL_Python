num, cnt = map(int, input().split())
inCnt = 0

for i in range(1, num + 1):
    if num % i == 0:
        inCnt += 1
    if inCnt == cnt:
        print(i)
        break

if inCnt != cnt:
    print(0)
