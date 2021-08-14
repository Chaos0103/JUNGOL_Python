num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

var = int(input())

result = [i for i in num if i % var == 0]

print(result)
