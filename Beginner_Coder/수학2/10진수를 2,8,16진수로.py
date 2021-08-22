num, num_type = map(int, input().split())


def binary_num(num):
    result = list()
    while True:
        result.append(num % 2)
        num //= 2
        if num == 0:
            break
    result.reverse()
    for idx in range(len(result)):
        print(result[idx], end='')


def octal_num(num):
    result = list()
    while True:
        result.append(num % 8)
        num //= 8
        if num == 0:
            break
    result.reverse()
    for idx in range(len(result)):
        print(result[idx], end='')


def hexadecimal_num(num):
    result = list()
    while True:
        var = (num % 16)
        if var >= 10:
             result.append(chr(ord('A') + (var - 10)))
        else:
            result.append(str(var))
        num //= 16
        if num == 0:
            break
    result.reverse()
    for idx in range(len(result)):
        print(result[idx], end='')


if num_type == 2:
    binary_num(num)
elif num_type == 8:
    octal_num(num)
elif num_type == 16:
    hexadecimal_num(num)
