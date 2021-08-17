import math

num = int(input())
result = list()

sqrt = int(math.sqrt(num))

for i in range(1, sqrt + 1):
    if num % i == 0:
        result.append(i)
        if num//i != i:
            result.append(num // i)

result.sort()

for idx in range(len(result)):
    print(result[idx], end=' ')
