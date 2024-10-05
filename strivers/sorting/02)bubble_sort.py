#q)bubble sort
def bubbleSort(arr1,size):
    #to loop through all the elements
    for j in range(size):
        #to loop till last element in unsorted array
        for i in range(size-j-1):
            #checking if next element is smaller, if yes sort it out
            if arr1[i+1]<arr1[i]:
                #swapping it
               arr1[i],arr1[i+1]=arr1[i+1],arr1[i]
    print(arr1)

arr1=[13,46,24,52,20, 9]
arr2=bubbleSort(arr1,len(arr1))
