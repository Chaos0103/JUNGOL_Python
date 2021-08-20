biNum = int(input())
mul = 1
result = 0
while True:
    result += (biNum % 10) * mul
    mul *= 2
    biNum //= 10
    if biNum == 0:
        break

print(result)
