#remove characters from
# odd indexes [PYTHON]

str = "Technology Encroyable"
newStr = ""
i = 0 
while i<len(str):
    if(i%2==0):
        newStr += str[i]
        i += 1 
    i+= 1 
          
print(newStr)    
       
