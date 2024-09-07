#q=>https://takeuforward.org/pattern/pattern-15-reverse-letter-triangle-pattern/
def nLetterTriangle(n: int):
    # Write your solution here.
    for i in range(n,0,-1):
        for j in range(ord('A'),ord('A')+i):
            print(chr(j),end=" ")
        print()
    pass
