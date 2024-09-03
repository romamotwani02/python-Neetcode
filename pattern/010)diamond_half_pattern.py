def nStarTriangle(n: int) -> None:
    # Write your code here.
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        for k in range(n-i-1):
            print(" ",end="")
        print()
    for j in range(n-2,-1,-1):
        for k in range(j+1):
            print("*",end="")
        for l in range(n-j-1):
            print(" ",end="")
        print()

    pass
  #forn=3,for n=5 different code

n=5
for i in range(1,(2*n-1)+1):
    stars=i
    if i>n:
        stars=2*n-i
    for j in range(stars):
        print("*",end="")
    print()

#easy way
def print_pattern(N):
    # Print the increasing part
    for i in range(1, N + 1):
        print('*' * i)
    
    # Print the decreasing part
    for i in range(N - 1, 0, -1):
        print('*' * i)
