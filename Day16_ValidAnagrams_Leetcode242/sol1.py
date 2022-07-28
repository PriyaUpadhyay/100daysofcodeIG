def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)
    
    # Counter("anagram")--> { 'a':3, 'n':1, 'g':1, 'r':1, 'm':1 }
