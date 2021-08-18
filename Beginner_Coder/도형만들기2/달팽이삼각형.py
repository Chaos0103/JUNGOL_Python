inNum = -1
front_idx = -1
back_idx = -1

def slide(num):
    idx(1, 1)
    num[front_idx][back_idx] = inNum

def left(num):
    idx(0, -1)
    num[front_idx][back_idx] = inNum

def up(num):
    idx(-1, 0)
    num[front_idx][back_idx] = inNum

def idx(FIdx, BIdx):
    global front_idx
    global back_idx
    global inNum
    front_idx += FIdx
    back_idx += BIdx
    inNum += 1
    if inNum == 10:
        inNum = 0

height = int(input())

num_list = [[0] * height for _ in range(height)]
cnt = height

for i in range(height):
    for _ in range(cnt):
        if i % 3 == 0:
            slide(num_list)
        elif i % 3 == 1:
            left(num_list)
        else:
            up(num_list)
    cnt -= 1

for i in range(height):
    for j in range(i + 1):
        print(num_list[i][j], end=' ')
    print('')
