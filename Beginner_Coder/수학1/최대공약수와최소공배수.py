import math
result1 = 0
result2 = 0

num1, num2 = map(int, input().split())
max = 0
min = 0
if num1 > num2:
    max = num1
    min = num2
else:
    max = num2
    min = num1

sqrt = int(math.sqrt(min))
min_list = list()

for i in range(1, sqrt + 1):
    if min % i == 0:
        min_list.append(i)
        if min // i != i:
            min_list.append(min // i)

min_list.sort(reverse=True)

for i in min_list:
    if max % i == 0:
        result1 = i
        break

for i in range(1, min + 1):
    if (max * i) % min == 0:
        result2 = max * i
        break

print(result1)
print(result2)
