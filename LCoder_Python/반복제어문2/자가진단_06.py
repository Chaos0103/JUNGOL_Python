cnt3 = 0
cnt5 = 0

num = list(map(int, input().split()))

for idx in range(10):
    if num[idx] % 3 == 0:
        cnt3 += 1
    if num[idx] % 5 == 0:
        cnt5 += 1

print('Multiples of 3 :', cnt3)
print('Multiples of 5 :', cnt5)
