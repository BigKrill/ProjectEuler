#!/usr/bin/env python3
largestNum = 0
palinNum = 0
def palindromic_num(n):
    numRev = []
    numSplit = list(str(n))
    i = len(numSplit)
    while i > 0 :
        numRev.append(numSplit[i-1])
        i -= 1
    
    for i in range(len(numSplit)):
        if numRev[i] != numSplit[i]:
            return False
    return True

for i in range(999):
    for j in range(999):
        if palindromic_num(i*j):
            palinNum = i*j
            if palinNum > largestNum:
                largestNum = palinNum

print(largestNum)
