#q=>https://takeuforward.org/pattern/pattern-14-increasing-letter-triangle-pattern/
def nLetterTriangle(n: int) -> None:
    # Write your solution here.
    for i in range(1,n+1):
        for j in range(ord("A"),ord("A")+i):
              print(chr(j),end=" ")
        print()
    pass
