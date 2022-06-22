# Interchange first and last 
# element in python
# 1st approcah - swapping

lst = [1,2,3,4,5]
size = len(lst)
temp = lst[0]
lst[0]=lst[size-1]
lst[size-1] = temp

print("  New List: ",lst)


# 2nd approcah - Interchanging using lst[-1] 

lst = [1,2,3,4,5]

lst[0], lst[-1] = lst[-1], lst[0]

print("  New List: ",lst)




# 3rd approcah - swap using a tuple

list = [1,2,3,4,5]

#storing in tuple
tup = list[-1],list[0]

#getback from tuple
list[0], list[-1] = tup 

print("  New List: ",list)




# 4th approcah - *operand

list = [1,2,3,4,5]

start ,*middle , end = list

list = [end, *middle, start]

print(list)




# 5th approcah - using pop() & insert()

list = [1,2,3,4,5]

start = list.pop(0)
end = list.pop(-1)

list.insert(0,end)
list.append(start)


print(list)



