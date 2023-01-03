import time
import math

str = time.time()

max_num = 1000

multiples = []
sum3=max_num//3*3*(max_num//3+1)/2
sum5=max_num//5*5*(max_num//5+1)/2
sum15=max_num//15*15*(max_num//15+1)/2
print(sum3+sum5-sum15)
sum=0
for i in range(1, max_num + 1):
    if i % 3 == 0 or i % 5 == 0:
        multiples.append(i)
        sum+=i

print(sum)
stp = time.time()
print(stp - str)


#n*n+1/2




