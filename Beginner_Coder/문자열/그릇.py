dish = input()

height = 10

for i in range(1, len(dish)):
    if dish[i-1] == dish[i]:
        height += 5
    else:
        height += 10

print(height)
