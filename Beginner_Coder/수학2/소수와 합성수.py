num = list(map(int, input().split()))

def prime(num):
    if num < 1:
        return False
    i = 2
    while i <= (num // i):
        if num % i == 0:
            return False
        i += 1
    return True

for var in num:
    if var == 1:
        print('number one')
        continue
    result = prime(var)
    if result:
        print('prime number')
    else:
        print('composite number')
