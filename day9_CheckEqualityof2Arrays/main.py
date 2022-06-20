
def checkEquality(arr1,arr2,len1,len2):
    if(len1!=len2):
        return False
    arr1.sort()
    arr2.sort()
    
    for i in range(0,len1):
        if(arr1[i]!=arr2[i]):
            return False
    return True

#driver code    
arr1 = [10, 30, 50, 20, 100]
arr2 = [30, 10, 100, 20, 50]
arr3 = [50, 60, 80, 10, 69]

l1 = len(arr1)
l2 = len(arr2)
l3 = len(arr3)

equality1 = checkEquality(arr1,arr2,l1,l2)
equality2 = checkEquality(arr1,arr3,l1,l3)

if(equality1): print("arr1 & arr2 are Equal.")
else: print("arr1 & arr2 are not Equal.")

if(equality2): print("arr1 & arr3 are Equal.")
else: print("arr1 & arr3 are not Equal.")
