size = int(input())
num_list = list(map(int, input().split()))
num = int(input())

sum1 = 0
sum2 = 0

for i in num_list:
    if num % i == 0:
        sum1 += i
    if i % num == 0:
        sum2 += i

print(sum1)
print(sum2)
