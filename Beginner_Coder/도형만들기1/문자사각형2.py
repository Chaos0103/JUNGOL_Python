size = int(input())

char_array = [['A'] * size for _ in range(size)]
inChar = 'A'

for i in range(size):
    for j in range(size):
        if i % 2 == 0:
            char_array[j][i] = inChar
        else:
            char_array[size - 1 - j][i] = inChar
        inChar = chr(ord(inChar) + 1)
        if inChar > 'Z':
            inChar = 'A'

for i in range(size):
    for j in range(size):
        print(char_array[i][j], end=' ')
    print('')
