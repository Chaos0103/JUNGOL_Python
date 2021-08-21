weight = [16, 8, 4, 2, 1]
num = list(map(int, input().split()))
cnt = 0
idx = 4
for var in weight:
    if num[5] // var > 0:
        if num[5] // var > num[idx]:
            num[5] -= (var * num[idx])
            cnt += num[idx]
        else:
            cnt += (num[5] // var)
            num[5] %= var
    idx -= 1

if num[5] == 0:
    print(cnt)
else:
    print('impossible')
