import math

def GCD(a, b):
    Fnum = list()
    for var in range(1, int(math.sqrt(a)) + 1):
        if(a % var == 0):
            Fnum.append(var)
            if a // var != var:
                Fnum.append(a // var)
    Fnum.sort(reverse=True)
    for var in Fnum:
        if b % var == 0:
            return var

def LCM(a, b):
    mul = 1
    Max = max(a, b)
    Min = min(a, b)
    while True:
        if (Max * mul) % Min == 0:
            return Max * mul
        else:
            mul += 1

size = int(input())
num = list(map(int, input().split()))

gcd = num[0]
lcm = num[0]

for i in range(len(num) - 1):
    gcd = GCD(gcd, num[1 + i])
    lcm = LCM(lcm, num[1 + i])

print(gcd, lcm)
