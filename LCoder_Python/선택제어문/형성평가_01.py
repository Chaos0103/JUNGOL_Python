num1, num2 = map(int, input().split())

result = num1 - num2 if num1 > num2 else num2 - num1

print(result)
