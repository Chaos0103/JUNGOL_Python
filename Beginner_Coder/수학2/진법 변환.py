indata = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while True:
    a = list(map(str, input().split()))
    if a[0] == '0':
        break

    num1 = int(a[0])
    num2 = int(a[2])
    list_len = len((a[1]))
    num1_by_num = 0
    mul = 1

    # 10진수 변환
    for var in range(list_len):
        ch = a[1][list_len - 1 - var]
        if '0' <= ch and ch <= '9':
            ch_by_int = ord(ch) - ord('0')
        else:
            ch_by_int = ord(ch) - ord('A') + 10
        num1_by_num += ch_by_int * mul
        mul *= num1

    # 입력진수 변환
    result = list()
    while True:
        x = num1_by_num % num2
        result.append(indata[x])
        num1_by_num //= num2
        if num1_by_num == 0:
            break
    result.reverse()
    for idx in range(len(result)):
        print(result[idx], end='')
    print('')
