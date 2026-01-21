def nStarDiamond(n: int) -> None:
    # Write your code here.
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for k in range(i*2+1):
            print("*",end="")
        for l in range(n-i-1):
            print(" ",end="")
        print()
    for j in range(n-1,-1,-1):
        for i in range(n-j-1):
            print(" ",end="")
        for l in range(j*2+1):
            print("*",end="")
        for k in range(n-j-1):
            print(" ",end="")
        print()
    pass

#other way
n=5

for i in range(0,n):
 space=n-i-1
 star=i*2+1
 print(' '*space+'*'*star+' '*space)
for i in range(n-1,-1,-1):
 star2=i*2+1
 space2=n-i-1
 print(' '*space2+'*'*star2+' '*space2)





