# Binary search pyhton
# iterative approach
def binarySearch(arr, val):
    low  = 0
    high = len(arr) - 1
    mid = 0 
    
    while low<=high :
        mid =( low +high) // 2 
        
        if arr[mid]<val:
            low = mid+1 
            
        elif arr[mid]>val:
            high = mid-1
            
        else:
            return mid
        
    return -1    
           
arr = [10,20,30,40,50]
val  = 50
result = binarySearch(arr,val)
if result!= -1:
    print(val, "is present at index", str(result))
else:
    print(val, "is not present.")
