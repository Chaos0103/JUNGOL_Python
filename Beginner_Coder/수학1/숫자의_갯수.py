cnt_list = [0] * 10

num1 = int(input())
num2 = int(input())
num3 = int(input())

result = num1 * num2 * num3

while result != 0:
    cnt_list[result % 10] += 1
    result //= 10

for idx in range(10):
    print(cnt_list[idx])
