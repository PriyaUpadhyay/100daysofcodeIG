class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        dictW2 , result = defaultdict(int), []
        
        for word in words2:
            dictW = Counter(word)
            for kvp in dictW:
                dictW2[kvp] = max(dictW[kvp],dictW2[kvp])
        
        
        for word in words1:
            dictW = Counter(word)
            
            for kvp in dictW2:
                if dictW[kvp] < dictW2[kvp]: break
            else:
                result.append(word)
                
            
        return result            
                
            
        
