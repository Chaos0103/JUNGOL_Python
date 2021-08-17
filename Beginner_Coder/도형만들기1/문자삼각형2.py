size = int(input())

if not(1 <= size and size <= 100) or (size % 2 == 0):
    print('INPUT ERROR')
else:
    char_list = [[' '] * size for _ in range(size)]
    inChar = 'A'
    cnt = 1
    for i in range(size // 2 + 1):
        frontIdx = size // 2 - i
        backIdx = size // 2 - i
        for _ in range(cnt):
            char_list[frontIdx][backIdx] = inChar
            inChar = chr(ord(inChar) + 1)
            frontIdx += 1
            if inChar > 'Z':
                inChar = 'A'
        backIdx -= 1
        cnt += 2

    for i in range(size):
        for j in range(size // 2 + 1):
            print(char_list[i][j], end=' ')
        print('')
