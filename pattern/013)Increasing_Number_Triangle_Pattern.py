#q=>https://takeuforward.org/pattern/pattern-13-increasing-number-triangle-pattern/
def nNumberTriangle(n: int) -> None:
    # Write your solution here.
    count=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(count,end=" ")
            count+=1
        print()
        
    pass
