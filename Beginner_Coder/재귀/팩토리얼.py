def Factorial(Num):
    global  result
    if Num == 1:
        print('1! = 1')
        return 1
    print(f'{Num}! = {Num} * {Num - 1}!')
    result *= Num
    return Factorial(Num - 1)

num = int(input())
result = 1
Factorial(num)
print(result)
