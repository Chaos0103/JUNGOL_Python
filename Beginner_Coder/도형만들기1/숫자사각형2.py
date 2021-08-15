input_num = 1
idx = 0

height, width = map(int, input().split())

print_list = [0] * (height * width)


for i in range(height):
    for j in range(width):
        if (i + 1) % 2 == 1:
            input_num = i * width + (j + 1)
            print_list[idx] = input_num
        else:
            input_num = ((i + 1) * width) - j
            print_list[idx] = input_num
        idx += 1
idx = 0
for i in range(height):
    for j in range(width):
        print('%d' % print_list[idx], end=' ')
        idx += 1
    print('')
