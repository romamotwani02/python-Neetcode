#q=>https://takeuforward.org/pattern/pattern-12-number-crown-pattern/
def numberCrown(n: int) -> None:
    # Write your solution here.
    spaces=2*(n-1)
    for i in range(1,n+1):
        #numbers
        
        for j in range(i):
            print(j+1,end=" ")
        
        #spaces
        for j in range(spaces+1):
            print(" ",end="")
        
        #numbers
        for j in range(i,0,-1):
            print(j,end=" ")
        print()
        space=-2
    pass
