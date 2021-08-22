num1 = int(input())
num2 = int(input())


def prime(num):
    if num < 2:
        return False
    i = 2
    while i <= (num // i):
        if num % i == 0:
            return False
        i += 1
    return True


min = num2
sum = 0
for var in range(num1, num2 + 1):
    if prime(var):
        sum += var
        if var < min:
            min = var
if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)
