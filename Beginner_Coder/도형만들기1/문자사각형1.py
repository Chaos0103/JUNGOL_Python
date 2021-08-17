size = int(input())

char_array = [['A'] * size for _ in range(size)]
inChar = 'A'

for i in range(size):
    for j in range(size):
        char_array[size - 1 - j][size - 1 - i] = inChar
        inChar = chr(ord(inChar) + 1)
        if inChar > 'Z':
            inChar = 'A'

for i in range(size):
    for j in range(size):
        print(char_array[i][j], end=' ')
    print('')
