#!/usr/bin/env python3
import math
num = 600851475143
largestNum = 0

def is_prime(n):
    for x in range(2, math.floor(math.sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True

def largest_prime_factor(n):
    factors = []

    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if is_prime(i):
            if n % i == 0:
                pair = n / i
                factors.append(i)
                if is_prime(pair):
                    factors.append(pair)
    return sorted(factors)[-1]

print(largest_prime_factor(num))