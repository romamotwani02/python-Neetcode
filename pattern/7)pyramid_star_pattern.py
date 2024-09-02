def nStarTriangle(n: int) -> None:
    for i in range(n):
        #to print leading spaces
        for j in range((n-i-1)):
            print(" ",end="")
        #to print star
        for i in range(((i*2)+1)):
            print("*",end="")
        #to print trailing spaces
        for i in range((n-i-1)):
            print(" ",end="")
        print()
