i = 0
oddSquares = []
sum = 0 

while i < 352000 :
    if ( i % 2 ) == 1 :
        oddSquares.append(i*i)        
    i += 1

for x in oddSquares :
    sum += x

print(sum)