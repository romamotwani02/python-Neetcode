q)=>https://www.codingninjas.com/studio/problems/check-prime_624934?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from math import sqrt

n = int(input())

if n == 1:
    print("NO")
else:
    sqrtd = int(sqrt(n))
    is_prime = True

    for i in range(2, sqrtd + 1):
        if n % i == 0:
            print("NO")
            is_prime = False
            break

    if is_prime:
        print("YES")
