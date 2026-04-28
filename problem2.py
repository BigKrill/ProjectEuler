#!/usr/bin/env python3

num1 = 1
num2 = 2
fibSum = 0
sum = num2
# def fibonacci(n):
#     if (n <= 1):
#         return n
#     return fibonacci(n-1)+fibonacci(n-2) 

while fibSum < 4000000:
    # print(fibonacci(i))

    fibSum = num1 + num2
    num1 = num2
    num2 = fibSum

    if fibSum % 2 == 0 and fibSum < 4000000:
        # print(f"add {fibSum}")
        sum += fibSum

print(sum)