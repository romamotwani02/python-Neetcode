#q)=>https://leetcode.com/problems/reverse-integer/description/
class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        is_negative=False

        if x<0:
            is_negative=True
            x*=-1
        while x>0:
            digit=x%10
            rev=rev*10+digit
            x=x//10
        

        return -rev if is_negative else rev


""" other approach
  class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        if x < 0:
            is_negative = True
            x *= -1

        res = 0
        while x > 0:
            digit = x % 10
            x //= 10
            if (res > (2 ** 31 - 1) // 10) or (res == (2 ** 31 - 1) // 10 and digit > 7):
                return 0
            res = (res * 10) + digit

"""
