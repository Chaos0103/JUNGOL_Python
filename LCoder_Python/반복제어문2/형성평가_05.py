even_cnt = 0
odd_cnt = 0

num = list(map(int, input().split()))

for idx in range(len(num)):
    if num[idx] % 2 == 0:
        even_cnt += 1
    elif num[idx] % 2 == 1:
        odd_cnt += 1

print('even :', even_cnt)
print('odd :', odd_cnt)
