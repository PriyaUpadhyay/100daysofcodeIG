# Interchange first and last 
# element in python
# 1st approcah - swapping

lst = [1,2,3,4,5]
size = len(lst)
temp = lst[0]
lst[0]=lst[size-1]
lst[size-1] = temp

print("  New List: ",lst)

