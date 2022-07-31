public class Solution {
    public IList<string> WordSubsets(string[] words1, string[] words2) 
    {
        List<string> result =  new List<string>();
        Dictionary<char,int> subString = CreateSubstringDict(words2);
        
        foreach(string word in words1){
            if(IsSubString(word,subString)){
                result.Add(word);
             }
        }
        return result;
    }
    public bool IsSubString(string word, Dictionary<char,int> subString){
        Dictionary<char,int> dictW = new Dictionary<char,int>();
        
        foreach(char c in word){
            if(dictW.ContainsKey(c))
                dictW[c]+=1;
            else
                dictW[c]=1;
        }
        
        foreach(var kvp in subString){
            if(dictW.ContainsKey(kvp.Key)){
                if(dictW[kvp.Key]< kvp.Value){
                    return false;
                }
            }
            else
                return false;
        }
        return true;
    }
    public Dictionary<char, int> CreateSubstringDict(string[] words2){
        Dictionary<char, int> result = new Dictionary<char,int>();
        foreach(string word in words2){
            Dictionary<char,int> temp = new Dictionary<char,int>();
            foreach(char c in word){
                if(temp.ContainsKey(c)){
                    temp[c] +=1;
                }else{
                    temp[c]=1;
                }
            }
            foreach(var kvp  in temp){
                if(result.ContainsKey(kvp.Key)){
                    if(result[kvp.Key]< kvp.Value){
                        result[kvp.Key] = kvp.Value;
                    }
                }
                else{
                    result.Add(kvp.Key,kvp.Value);
                }
            }
        }
        return result;
    }
}
    
    
