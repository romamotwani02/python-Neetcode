def nNumberTriangle(n: int) -> None:
    # Write your solution here.
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
