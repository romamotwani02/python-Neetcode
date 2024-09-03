def nForest(n:int) ->None:
   for i in range(n):
       for j in range(i+1):
           print("*",end=" ")
       print("")

#another way
#for i in range(1, 4):  # Loop through 1 to 3
#    print("* " * i)   # Print '*' i times
