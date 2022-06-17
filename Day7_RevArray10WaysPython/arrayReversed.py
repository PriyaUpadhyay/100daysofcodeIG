# reverse array in python
# 10 different ways

# 2. using reverserd()
import array
arr = array.array('i',[10,20,30,40,50])
print(" Original : ",arr)
rev = array.array('i',reversed(arr))
print(" Reversed : ",rev)
