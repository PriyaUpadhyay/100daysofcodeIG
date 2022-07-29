public class Solution {
    public IList<string> FindAndReplacePattern(string[] words, string pattern)
    {
        List<string> result =  new List<string>();
        foreach(string word in words){
            if(checkPattern(word, pattern)){
                result.Add(word);
            }
            
        }
        return result;
        
    }
    public bool checkPattern(string word, string pattern){
        if(word.Length == pattern.Length)
        {
            Dictionary<char , char> patternToWord = new Dictionary<char, char>();
            Dictionary<char , char> wordToPattern = new Dictionary<char, char>();
            for(int i = 0;i<word.Length;i++){
                if(patternToWord.ContainsKey(pattern[i])){
                    if(patternToWord[pattern[i]] != word[i]){
                        return false;
                    }
                }
                else{
                    patternToWord[pattern[i]] =  word[i];
                }
            }
            
            
            for(int i = 0;i<word.Length;i++){
                if(wordToPattern.ContainsKey(word[i])){
                    if(wordToPattern[word[i]] != pattern[i]){
                        return false;
                    }
                }
                else{
                    wordToPattern[word[i]] =  pattern[i];
                }
            }
            return true;
                
        }
        
        return false;
    }
}
