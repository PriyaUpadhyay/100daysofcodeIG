def mergeArrays(aar1, arr2, l1, l2):
    arr3 = [None]*(l1+l2)
    i = 0
    j = 0
    k = 0
    while i<l1 and j<l2:
        if arr1[i]<arr2[j]:
            arr3[k] = arr1[i]
            i = i + 1
            k = k + 1 
        else:
            arr3[k]= arr2[j]
            k = k+1 
            j = j+1 
    while i<l1:
        arr3[k] = arr1[i]
        i = i + 1
        k = k + 1 
    while j< l2:
        arr3[k]= arr2[j]
        k = k+1 
        j = j+1 
        
    return arr3
    

arr1 = [1,4,6,9]
l1 = len(arr1)

arr2 = [3,5,7,10]
l2 = len(arr2)
      
arr3 = mergeArrays(arr1, arr2, l1,l2)
print("\nMerged Array: ")
for i in range(l1+l2):
        print(str(arr3[i]), end = " ")
    
    
