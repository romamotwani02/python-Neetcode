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


#another way
rows = 5
for i in range(1, rows + 1):
 left_spaces = rows-i
 stars = 2*i-1
 right_spaces = rows - i

 print(" " * left_spaces + "*" * stars + " " * right_spaces)

#another way 

n=5
for i in range(0,n):
 space-n-i-1
 star=i*2+1
 print(' '*space+"*"*star+' '*space)


