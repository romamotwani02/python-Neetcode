#question->https://takeuforward.org/pattern/pattern-11-binary-number-triangle-pattern/

def nBinaryTriangle(n: int) -> None:
    # Write your solution here.
    for i in range(n):
        start=0
        if i%2==0:
            start=1
        for j in range(i+1):
            print(start,end=" ")
            start=1-start
        print()

          
    pass
