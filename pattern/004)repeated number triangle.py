def triangle(n:int) ->None:
    for i in range(n):
        for j in range(i):
            print(i,end=" ")
        print()

#another way
#def triangle(n:int) ->None:
#    for i in range(1, n+1):  # Loop from 1 to 3
#        print((str(i) + " ") * i) 
