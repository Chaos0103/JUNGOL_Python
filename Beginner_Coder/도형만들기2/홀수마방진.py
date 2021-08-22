size = int(input())

input_num = 1
front_index = 0
back_index = size // 2


def left_up(num_list):
    num_list[front_index][back_index] = input_num
    move_idx(-1, -1)


def down(num_list):
    num_list[front_index][back_index] = input_num
    move_idx(1, 0)


def swap():
    global front_index
    global back_index
    if front_index == -1:
        front_index += size
    else:
        back_index += size


def move_idx(fidx, bidx):
    global front_index
    global back_index
    global input_num
    front_index += fidx
    back_index += bidx
    input_num += 1
    if (front_index == -1) or (back_index == -1):
        swap()


num = [[0] * size for _ in range(size)]

for i in range(1, size*size+1):
    if i % size == 0:
        down(num)
        continue
    left_up(num)

for i in range(size):
    for j in range(size):
        print(num[i][j], end=' ')
    print('')
