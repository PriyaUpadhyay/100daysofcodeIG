import os

def compute(fname):
    words = 0
    lines = 0
    chars = 0
    spaces = 0
    with open(fname,'r') as file:
        for line in file:
            line = line.strip(os.linesep)
            wordList = line.split()
            lines +=1
            words += len(wordList)
            chars += sum(1 for c in line
                         if c not in(os.linesep,' '))
            spaces += sum(1 for s in line
                          if s in (os.linesep,' '))
    print("words :",words)
    print("lines :",lines)
    print("characters:",chars)
    print("spaces: ",spaces)
    
if __name__ == '__main__':
    fname = "Input.txt"
    try:
        compute(fname)
    except:
        print('File not found.')    
    
