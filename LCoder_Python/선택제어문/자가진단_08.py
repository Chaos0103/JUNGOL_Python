num1, num2, num3 = map(int, input().split())

min = num1 if num1 < num2 else num2
min = min if min < num3 else num3

print(min)
