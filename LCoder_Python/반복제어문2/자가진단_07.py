sum = 0

num = list(map(int, input().split()))

for idx in range(len(num)):
    sum += num[idx]
    
avg = sum / len(num)

print('avg : %.1f' % avg)
if avg >= 80:
    print('pass')
else:
    print('fail')
