key = input()
code = input()

for idx in range(len(code)):
    if 'A' <= code[idx] and code[idx] <= 'Z':
        key_idx = ord(code[idx]) - ord('A')
        print(chr(ord(key[key_idx]) - ord('a') + ord('A')), end='')
    elif 'a' <= code[idx] and code[idx] <= 'z':
        key_idx = ord(code[idx]) - ord('a')
        print(key[key_idx], end='')
    else:
        print(end=' ')
