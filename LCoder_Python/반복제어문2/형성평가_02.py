num1, num2 = map(int, input().split())

if num1 > num2:
    tmp = num1
    num1 = num2
    num2 = tmp

for i in range(num1, num2 + 1):
    print(i)
