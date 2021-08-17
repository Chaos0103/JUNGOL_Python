size = int(input())

char_list = [[' '] * size for _ in range(size)]
inChar = 'A'

for i in range(size):
    frontIdx = i
    backIdx = size - 1
    for _ in range(size - i):
        char_list[frontIdx][backIdx] = inChar
        inChar = chr(ord(inChar) + 1)
        frontIdx += 1
        backIdx -= 1
        if inChar > 'Z':
            inChar = 'A'

for i in range(size):
    for j in range(size):
        print(char_list[i][j], end=' ')
    print('')
