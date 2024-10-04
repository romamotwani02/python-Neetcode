
def selectionSort(arr1,size):
    for i in range(size):
        min_idx=i
        for j in range(i+1,size):
            if arr1[j]<arr1[min_idx]:
                min_idx=j
        arr1[i],arr1[min_idx]=arr1[min_idx],arr1[i]
    return arr1



arr1 = [-2, 45, 0, 11, -9,88,-97,-202,747]
size=len(arr1)
arr2=selectionSort(arr1,size)
print(arr2)
#output-[-202, -97, -9, -2, 0, 11, 45, 88, 747]
