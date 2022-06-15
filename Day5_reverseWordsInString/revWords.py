#reverse string in python

word = "Technology Encroyable"

words = word.split(' ')
revArr = []

for wor in words:
    revArr.insert(0,wor)
    
print(' '.join(revArr))
