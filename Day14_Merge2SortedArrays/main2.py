# Python program to merge two sorted arrays
# using bisect module

import bisect

def mergeArrays(arr1, arr2, l1, l2):
    arr3 = []
    for i in range(l1):
        bisect.insort(arr3, arr1[i])
    for i in range(l2):
        bisect.insort(arr3, arr2[i])
        
    return arr3        
   

arr1 = [1, 4, 6, 9]
arr2 = [3, 5, 7, 10]
l1 = len(arr1)
l2 = len(arr2)

arr3 = mergeArrays(arr1, arr2, l1, l2)
print("\nMerged Array: ")
for i in range(l1+l2):
        print(str(arr3[i]), end = " ")
    
      
    
