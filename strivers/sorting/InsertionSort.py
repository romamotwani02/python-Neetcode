def InsertionSort(arr,size):
    #to loop through all the elements
    for i in range(size):
      #loop till 1 or 2 or 3...n 
      j=i
      # till 1 or 2..while element is previous element is greater sort 
      while j>0 and arr[j-1]>arr[j]:
           arr[j],arr[j-1]=arr[j-1],arr[j]
           j-=1 #go from value comapring first (3,2) then(2,1), then (1,0) when i=3
    print(arr)
        


arr1=[13,46,24,52,20, 9]
arr2=InsertionSort(arr1,len(arr1))
