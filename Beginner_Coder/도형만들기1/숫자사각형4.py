def type_01(data):
    for i in range(1, data + 1):
        for _ in range(data):
            print(i, end=' ')
        print('')

def type_02(data):
    for i in range(1, data + 1):
        odd = 1
        even = data
        for _ in range(data):
            if i % 2 == 1:
                print(odd, end=' ')
                odd += 1
            else:
                print(even, end=' ')
                even -= 1
        print('')

def type_03(data):
    for i in range(1, data + 1):
        for j in range(1, data + 1):
            print(i * j, end=' ')
        print('')

size, type = map(int, input().split())

if type == 1:
    type_01(size)
elif type == 2:
    type_02(size)
elif type == 3:
    type_03(size)
