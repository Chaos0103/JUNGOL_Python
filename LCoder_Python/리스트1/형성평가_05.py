num = list(map(str, input().split()))

result = [ch for ch in num if num.index(ch) % 3 == 2]

print(result)
