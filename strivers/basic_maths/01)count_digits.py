#q)=>https://www.naukri.com/code360/problems/count-digits_8416387?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def countDigits(n: int) -> int:
    counter=0
    temp=n
    while n>0:
        digit=n%10
        n=n//10
        if digit!=0:
            if temp%digit==0:
                counter+=1
    return counter
    pass
