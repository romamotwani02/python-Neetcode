#q)-> find divisors of the number
import math
print("enter a number to find its divisors")
n=int(input())
l1=[]
sqrt=int(math.sqrt(n))
for i in range(1,sqrt+1):
    if n%i==0:
        l1.append(i)
        l1.append((n//i))
print(l1)
