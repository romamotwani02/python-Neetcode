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

#other way
n=4
for i in range(1,n+1):
 for j in range(1,i+1):
  print(j,end='')
 spaces=2*(n-i)
 for k in range(1, spaces+1):
  print(" ",end='')
 for l in range(i,0,-1):
  print(l,end='')
  print()

