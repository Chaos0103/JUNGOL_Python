num1, size1 = map(int, input().split())
num2, size2 = map(int, input().split())

result1 = [num1 for _ in range(size1)]
result2 = [num2 for _ in range(size2)]

result = result1 + result2

print(result)
