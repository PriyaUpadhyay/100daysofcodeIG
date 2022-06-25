# Binary search pyhton
# recursive approach
def binarySearch(arr,  low , high , val):
    if high>=low:
        mid = high +low // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            return binarySearch(arr , low , mid-1 , val)
        else:
            return binarySearch(arr, mid+1, high , val)
    else:
        return -1
           
arr = [10,20,30,40,50]
val  = 250
result = binarySearch(arr, 0 , len(arr)-1, val)
if result!= -1:
    print(val, "is present at index", str(result))
else:
    print(val, "is not present.")
