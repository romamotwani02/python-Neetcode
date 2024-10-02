q)=>https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1
class Solution:
    def armstrongNumber (self, n):
        # code here 
        temp=n
        arm=0
        power=len(str(n))
        while n>0:
            digit=n%10
            arm+=digit**power
            n=n//10
        if temp==arm:
            return "true"
        else:
            return "false"

