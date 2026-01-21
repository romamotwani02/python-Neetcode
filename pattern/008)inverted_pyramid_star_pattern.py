def nStarTriangle(n: int) -> None:
    # Write your code here.
 for i in range(n-1,-1,-1):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i*2+1):
        print("*",end="")
    for l in range(n-i-1):
        print(" ",end="")
    print()
    
    
#other way
n=5
for i in range(n-1,-1,-1):
 space=n-i-1
 star=i*2+1
 print('  '*space+"*"*star+'  '*space)
