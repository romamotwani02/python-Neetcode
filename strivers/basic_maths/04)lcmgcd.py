q)=>https://www.geeksforgeeks.org/problems/lcm-and-gcd4516/1
class Solution:
    def lcmAndGcd(self, A , B):
        # code here 
        product=A*B
        g=0
        while (A>0 and B>0):
            if A>B:
                A=A%B
            else:
                B=B%A
        if A==0:
            g=B
        else:
            g=A
            
        l=(product)//g
        return l,g 

"""
find gcd by euclidean method, lcm is product of two number divided by gcd or take maximum of larger number, inside while loop
divide larger number by both number if it returns zero, then it is lcm if not increment it by larger number
step=larger
while true:
  if larger%A==0 and larger%B==0:
    return larger
  larger+=step
"""
