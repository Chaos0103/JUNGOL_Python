odd_cnt = 0
even_cnt = 0

while True:
    num = int(input())
    if num == 0:
        break
    elif num % 2 == 0:
        even_cnt += 1
    elif num % 2 == 1:
        odd_cnt += 1

print('odd :', odd_cnt)
print('even :', even_cnt)
