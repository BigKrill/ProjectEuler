#!/usr/bin/env python3
import time

num = 1
start = time.time()
limit = 20
while True:
    for i in range(0, limit):
        if num % (i+1) == 0:
            
            continue
        else:
            break
    if i+1 == limit :
        break
    num += 1

end = time.time()

print(end-start)
print(num)