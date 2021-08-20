while True:
    num = int(input())
    if num == 0:
        break
    sum = 0
    result = 0
    while True:
        result = result * 10 + num % 10
        sum += num % 10
        num //= 10
        if num == 0:
            break
    print(result, sum)
