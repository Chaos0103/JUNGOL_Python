height, width = map(int, input().split())

num_print = 1

for _ in range(height):
    for _ in range(width):
        print(num_print, end=' ')
        num_print += 1
    print('')
