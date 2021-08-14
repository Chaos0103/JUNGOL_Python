cnt = 0

while True:
    num = int(input())
    if num == 0:
        break
    if not(num % 3 == 0 or num % 5 == 0):
        cnt += 1

print(cnt)
